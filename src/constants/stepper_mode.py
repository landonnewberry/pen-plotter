from typing import Tuple
from RPi.GPIO import HIGH, LOW


class StepperMode:
    step_delay_ms: int
    voltages: Tuple[any]
    rotation_multiplier: int

    def __init__(
        self, step_delay_ms: int, voltages: Tuple[any], rotation_multiplier: int
    ) -> None:
        self.step_delay_ms = step_delay_ms
        self.voltages = voltages
        self.rotation_multiplier = rotation_multiplier


class StepperModes:
    FULL: StepperMode = StepperMode(
        step_delay_ms=50, voltages=(LOW, LOW, LOW), rotation_multiplier=1
    )

    HALF: StepperMode = StepperMode(
        step_delay_ms=50, voltages=(HIGH, LOW, LOW), rotation_multiplier=2
    )

    QUARTER: StepperMode = StepperMode(
        step_delay_ms=70, voltages=(LOW, HIGH, LOW), rotation_multiplier=4
    )

    EIGHTH: StepperMode = StepperMode(
        step_delay_ms=20, voltages=(HIGH, HIGH, LOW), rotation_multiplier=8
    )

    SIXTEENTH: StepperMode = StepperMode(
        step_delay_ms=20, voltages=(LOW, LOW, HIGH), rotation_multiplier=16
    )

    THIRTYSECOND: StepperMode = StepperMode(
        step_delay_ms=20, voltages=(HIGH, LOW, HIGH), rotation_multiplier=32
    )
