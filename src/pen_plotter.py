from config import Config
from constants.stepper_mode import StepperModes
from motor import Direction, Motor
from constants import pinouts, motor_specs

motor1: Motor = Motor(
    step_pin=pinouts.M1_STEP_PIN,
    direction_pin=pinouts.M1_DIR_PIN,
    mode_pins=(pinouts.M0_PIN, pinouts.M1_PIN, pinouts.M2_PIN),
    steps_per_rotation=motor_specs.STEPS_PER_ROTATION,
)

motor2: Motor = Motor(
    step_pin=pinouts.M2_STEP_PIN,
    direction_pin=pinouts.M2_DIR_PIN,
    mode_pins=(pinouts.M0_PIN, pinouts.M1_PIN, pinouts.M2_PIN),
    steps_per_rotation=motor_specs.STEPS_PER_ROTATION,
)


class PenPlotter:
    config: Config

    def __init__(self) -> None:
        self.config = Config()
        motor1.set_acceleration(rotation_percentage=100, growth_factor=20)
        motor2.set_acceleration(rotation_percentage=100, growth_factor=20)

    def run(self) -> None:
        print("Motor 1 going")
        motor1.move(Direction.CW, 200, StepperModes.SIXTEENTH)
        motor1.move(Direction.CCW, 200 * 2, StepperModes.SIXTEENTH)
        motor1.move(Direction.CW, 200, StepperModes.SIXTEENTH)

        print("Motor 2 going")
        motor2.move(Direction.CW, 200, StepperModes.SIXTEENTH)
        motor2.move(Direction.CCW, 200 * 2, StepperModes.SIXTEENTH)
        motor2.move(Direction.CW, 200, StepperModes.SIXTEENTH)
