import math
from typing import List, Tuple
import RPi.GPIO as GPIO
from enum import Enum
from constants.stepper_mode import StepperModes, StepperMode
from utils import delay_ms


class Direction(Enum):
    CW = 1
    CCW = 0


class Motor:

    step_pin: int
    direction_pin: int
    mode_pins: Tuple[int]
    step_mode: StepperMode
    steps_per_rotation: int

    _acceleration_step_delays: List[float]

    def __init__(
        self,
        step_pin: int,
        direction_pin: int,
        mode_pins: Tuple[int],
        steps_per_rotation: int,
        step_mode: StepperMode = StepperModes.SIXTEENTH,
    ) -> None:
        self.step_pin = step_pin
        self.direction_pin = direction_pin
        self.mode_pins = mode_pins
        self.steps_per_rotation = steps_per_rotation
        self.step_mode = step_mode
        self._acceleration_step_delays = []

    def set_mode(self, mode: StepperMode) -> None:
        try:
            V0, V1, V2 = mode.voltages
            GPIO.output(self.mode_pins[0], V0)
            GPIO.output(self.mode_pins[1], V1)
            GPIO.output(self.mode_pins[2], V2)
        except Exception as ex:
            print(f"Error setting stepper motor mode: {ex}")
            raise

    def set_direction(self, direction: Direction) -> None:
        try:
            if direction.value:  # clockwise
                GPIO.output(self.direction_pin, GPIO.HIGH)
            else:  # counter-clockwise
                GPIO.output(self.direction_pin, GPIO.LOW)
        except Exception as ex:
            print(f"Error setting direction: {ex}")
            raise

    def set_acceleration(
        self, rotation_percentage: int = 50, growth_factor: int = 2
    ) -> None:
        """
        Inputs:
            rotation_percentage: How much of a rotation should it take for
            rotation to reach its full speed?
                i.e. rotation_percentage = 100, the speed of rotation (steps)
                     will reach its target speed after one full rotation of
                     the motor shaft
        """
        try:
            target_steps = (
                self.steps_per_rotation
                * rotation_percentage
                * 0.01
                * self.step_mode.rotation_multiplier
            )

            delay_target = self.step_mode.step_delay_ms
            delay_init = growth_factor * delay_target

            decay_rate = math.log(delay_target / delay_init, target_steps)

            acceleration_steps = []
            i = 1
            while i <= target_steps:
                acceleration_steps.append(delay_init * (i ** decay_rate))
                i += 1

            self._acceleration_step_delays = acceleration_steps
        except Exception as ex:
            print(f"Error while setting acceleration on stepper motor: {ex}")
            raise

    def move(self, direction: Direction, steps: int, mode: StepperMode = None) -> None:
        if not mode:
            mode = self.step_mode

        self.set_mode(mode)
        self.set_direction(direction)

        try:
            steps_to_take = steps * self.step_mode.rotation_multiplier
            for i in range(steps_to_take):
                if i < steps_to_take // 2 and i < len(self._acceleration_step_delays):
                    delay = self._acceleration_step_delays[i]
                elif steps_to_take - i < len(self._acceleration_step_delays):
                    delay = self._acceleration_step_delays[steps_to_take - i]
                else:
                    delay = self.step_mode.step_delay_ms

                GPIO.output(self.step_pin, GPIO.HIGH)
                delay_ms(delay)
                GPIO.output(self.step_pin, GPIO.LOW)
                delay_ms(delay)
        except Exception as ex:
            print(f"Error while pulsing the stepper motor {ex}")
            raise
