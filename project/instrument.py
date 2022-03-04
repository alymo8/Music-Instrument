#!/usr/bin/env python3

# TODO Add more details about your overall instrument implementation in the docstring below
"""
Simple musical instrument.
"""

from utils.brick import configure_ports  # TODO Add other devices (sensors or motors) here depending on your design

from utils import sound
from utils.brick import TouchSensor, EV3UltrasonicSensor, configure_ports, reset_brick
from time import sleep
# Add any additional imports in this area, at the top of the file

TOUCH_SENSOR, US_SENSOR = configure_ports(PORT_1=TouchSensor, PORT_2=EV3UltrasonicSensor)

DELAY_SEC = 0.01  # seconds of delay between measurements


# Define your classes and functions here. You may use other files, but you don't have to

def collect_discrete_us_data():
    try:
    
        while True:
            if TOUCH_SENSOR.is_pressed():
                us_data = US_SENSOR.get_value()  # Float value in centimeters 0, capped to 255 cm
                if us_data < 6.5 and us_data >= 2.5:
                   ORGAN_SOUNDS["E4"].play()
                   sleep(DELAY_SEC)
                if us_data < 14 and us_data >= 6.5:
                    ORGAN_SOUNDS["G4"].play()
                    sleep(DELAY_SEC)
                if us_data < 21 and us_data >= 14:
                    ORGAN_SOUNDS["A4"].play()
                    sleep(DELAY_SEC)
                if us_data < 28.25 and us_data >= 21:
                    ORGAN_SOUNDS["B4"].play()
                    sleep(DELAY_SEC)
#                 else:
#                     ORGAN_SOUNDS["G5"].play()
#                     sleep(DELAY_SEC) 
                    
                print(us_data)
                sleep(DELAY_SEC)
                while (TOUCH_SENSOR.is_pressed()):
                    pass
        
    except BaseException as e:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        pass
    
    finally:
        print("Done collecting US distance samples")
        exit()
    
if __name__ == "__main__":
    # this import needs to be here to allow sound module to load properly
    from utils.sound import *

    # TODO Start your instrument here by replacing the example below with a relevant function call from your own code
#     for note in ["C5", "D5", "E5", "F5", "G5", "A5", "B5"]:  # Do-Re-Mi
#         ORGAN_SOUNDS[note].play()
#         sleep(1)
    
    collect_discrete_us_data()
