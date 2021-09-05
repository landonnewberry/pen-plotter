import time
import RPi.GPIO as GPIO
from config import Config
from motor import Direction, Motor, StepMode
from constants import pinouts


motor1: Motor = Motor(
    step_pin=pinouts.M1_STEP_PIN,
    direction_pin=pinouts.M1_DIR_PIN,
    mode_pins=(pinouts.M0_PIN, pinouts.M1_PIN, pinouts.M2_PIN),
)

motor2: Motor = Motor(
    step_pin=pinouts.M2_STEP_PIN,
    direction_pin=pinouts.M2_DIR_PIN,
    mode_pins=(pinouts.M0_PIN, pinouts.M1_PIN, pinouts.M2_PIN),
)


class Main:
    config: Config

    def __init__(self) -> None:
        self.config = Config()

    def run(self) -> None:
        print("Motor 1 going")
        motor1.move(Direction.CW, 200 * 8, StepMode.EIGHTH)
        motor1.move(Direction.CCW, 200 * 2 * 8, StepMode.EIGHTH)
        motor1.move(Direction.CW, 200 * 8, StepMode.EIGHTH)

        print("Motor 2 going")
        motor2.move(Direction.CW, 200 * 8, StepMode.EIGHTH)
        motor2.move(Direction.CCW, 200 * 2 * 8, StepMode.EIGHTH)
        motor2.move(Direction.CW, 200 * 8, StepMode.EIGHTH)


app: Main = Main()

app.run()
