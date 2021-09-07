from DRV8825_driver.motor import Direction, Motor
from DRV8825_driver.stepper_mode import StepperModes
from constants import pinouts, motor_specs
from multiprocessing import Process


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


class Head:
    def __init__(self) -> None:
        motor1.set_acceleration(rotation_percentage=100, growth_factor=20)
        motor1.set_mode(StepperModes.SIXTEENTH)

        motor2.set_acceleration(rotation_percentage=100, growth_factor=20)
        motor2.set_mode(StepperModes.SIXTEENTH)

    @classmethod
    def move(cls, x: int, y: int):
        px1 = Process(
            target=motor1.move, args=(Direction.CCW if x >= 0 else Direction.CW, abs(x))
        )
        px2 = Process(
            target=motor2.move, args=(Direction.CW if x >= 0 else Direction.CCW, abs(x))
        )

        py1 = Process(
            target=motor1.move, args=(Direction.CCW if y >= 0 else Direction.CW, abs(y))
        )
        py2 = Process(
            target=motor2.move, args=(Direction.CCW if y >= 0 else Direction.CW, abs(y))
        )

        px1.start()
        px2.start()
        py1.start()
        py2.start()
        px1.join()
        px2.join()
        py1.join()
        py2.join()

    @staticmethod
    def _get_step_direction(d: int) -> Direction:
        return Direction.CCW if d >= 0 else Direction.CW

    @staticmethod
    def _get_opposite_direction(d: Direction) -> Direction:
        return Direction.CW if d.value == Direction.CCW.value else Direction.CCW
