#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, InfraredSensor)
from pybricks.parameters import Port, Button
from pybricks.tools import wait

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Set volume to 100% and make a beep to signify program has started
ev3.speaker.set_volume(100)
ev3.speaker.beep()

# Initialize EV3 touch sensor and motors
motorLeft = Motor(Port.A)
motorRight = Motor(Port.B)
infrared = InfraredSensor(Port.S1)

# Create a loop to react to buttons
while True:

    # Check for center button events
    if Button.CENTER in ev3.buttons.pressed():
        motorLeft.stop()
        motorRight.stop()
        break

    # React to the left up and down buttons
    if Button.LEFT_DOWN in infrared.keypad():
        motorLeft.dc(-50)
    elif Button.LEFT_UP in infrared.keypad():
        motorLeft.dc(50)
    else:
        motorLeft.stop()

    # React to the right up and down buttons
    if Button.RIGHT_DOWN in infrared.keypad():
        motorRight.dc(-50)
    elif Button.RIGHT_UP in infrared.keypad():
        motorRight.dc(50)
    else:
        motorRight.stop()

    # Uncomment to display the current status of the remote buttons
    # print("Buttons: ", infrared.buttons(1))

    # I have found the keypads method to be more accurate, but only works
    # with one remote on channel one
    # print("Keypad: ", infrared.keypad())

    # Uncomment to display the distance and angle of the remote
    # print("Remote: ", infrared.beacon(1))

    wait(10)

# Use the speech tool to signify the program has finished
ev3.speaker.say("Program complete")
