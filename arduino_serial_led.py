import serial
import time

def initialize(serial_port, bit_rate):
    """
    A function that returns the serial
    object to communicate with the Arduino
    """
    return serial.Serial(serial_port, bit_rate)
    # time.sleep(2)
    
def control_arduino_led(arduino_serial, led_state):
    """
    Control the arduino led using the serial
    """
    
    if led_state == "1": # if user wants to turn the led ON
        arduino_serial.write("1".encode()) # send "1" to the arduino over serial
        return "[LED TURNED ON]" # return success message

    elif led_state == "0": # if user wants to turn the led OFF
        arduino_serial.write("0".encode()) # send "0" to the arduino over serial
        return "[LED TURNED OFF]" # return success message

    else: # if the resquested led state is invalid (other than 1 or 0)
        return "[INVALID ARGUMENT SUPPLIED]" # print error message

    # time.sleep(1)
