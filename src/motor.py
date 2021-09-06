from typing import Tuple
import RPi.GPIO as GPIO
from RPi.GPIO import HIGH, LOW
from enum import Enum
from utils import delay_ms


class StepMode(Enum):
    FULL = 100
    HALF = 75
    QUARTER = 70
    EIGHTH = 60
    SIXTEENTH = 40
    THIRTYSECOND = 45


class Direction(Enum):
    CW = 1
    CCW = 0


step_mode_voltage_outputs: dict = {
    StepMode.FULL: (LOW, LOW, LOW),
    StepMode.HALF: (HIGH, LOW, LOW),
    StepMode.QUARTER: (LOW, HIGH, LOW),
    StepMode.EIGHTH: (HIGH, HIGH, LOW),
    StepMode.SIXTEENTH: (LOW, LOW, HIGH),
    StepMode.THIRTYSECOND: (HIGH, LOW, HIGH),
}


class Motor:

    step_pin: int
    direction_pin: int
    mode_pins: Tuple[int]
    step_mode: StepMode

    def __init__(
        self,
        step_pin: int,
        direction_pin: int,
        mode_pins: Tuple[int],
        step_mode: StepMode = StepMode.EIGHTH,
    ) -> None:
        self.step_pin = step_pin
        self.direction_pin = direction_pin
        self.mode_pins = mode_pins
        self.step_mode = step_mode

    def set_mode(self, mode: StepMode) -> None:
        try:
            V0, V1, V2 = step_mode_voltage_outputs[mode]
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

    def move(self, direction: Direction, steps: int, mode: StepMode = None) -> None:
        if not mode:
            mode = self.step_mode

        self.set_mode(mode)
        self.set_direction(direction)

        try:
            for _ in range(steps):
                GPIO.output(self.step_pin, GPIO.HIGH)
                delay_ms(mode.value)
                GPIO.output(self.step_pin, GPIO.LOW)
                delay_ms(mode.value)
        except Exception as ex:
            print(f"Error while pulsing the stepper motor {ex}")
            raise
