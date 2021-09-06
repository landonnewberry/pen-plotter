# Initialize the board
import RPi.GPIO as GPIO
from constants import pinouts


class Config:
    def __init__(self):
        GPIO.setwarnings(False)

        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(pinouts.M1_STEP_PIN, GPIO.OUT)
        GPIO.setup(pinouts.M1_DIR_PIN, GPIO.OUT)
        GPIO.setup(pinouts.M2_STEP_PIN, GPIO.OUT)
        GPIO.setup(pinouts.M2_DIR_PIN, GPIO.OUT)
        GPIO.setup(pinouts.M0_PIN, GPIO.OUT)
        GPIO.setup(pinouts.M1_PIN, GPIO.OUT)
        GPIO.setup(pinouts.M2_PIN, GPIO.OUT)
