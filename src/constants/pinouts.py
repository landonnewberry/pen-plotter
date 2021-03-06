# Controls:
# - Pulse step pins for a step
# - Drive direction pins high for CW, low for CCW
# - Mode pins control step size (bits specified in datasheet):
#   - 1, 1/2, 1/4, 1/8, 1/32

# Stepper Motor 1 (Lower Y Axis)
M1_STEP_PIN = 16
M1_DIR_PIN = 18

# Stepper Motor 2 (Upper Y Axis)
M2_STEP_PIN = 11
M2_DIR_PIN = 13

# Mode control pins on DRV8825
M0_PIN = 36
M1_PIN = 38
M2_PIN = 40
