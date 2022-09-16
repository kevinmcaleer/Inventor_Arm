from inventor import Inventor2040W, SERVO_1, SERVO_2, SERVO_3, SERVO_4, SERVO_5, SERVO_6 
from time import sleep
import math

board = Inventor2040W()

base = board.servos[SERVO_6]
base.enable()
elbow = board.servos[SERVO_5]
elbow.enable()

base.to_mid()
elbow.to_min()
sleep(1)

SWEEPS = 3              # How many sweeps of the servo to perform
STEPS = 10              # The number of discrete sweep steps
STEPS_INTERVAL = 0.5    # The time in seconds between each step of the sequence
SWEEP_EXTENT = 90.0     # How far from zero to move the servo when sweeping

# Do a sine sweep
for j in range(SWEEPS):
    for i in range(360):
        base.value(math.sin(math.radians(i)) * SWEEP_EXTENT)
        sleep(0.02)