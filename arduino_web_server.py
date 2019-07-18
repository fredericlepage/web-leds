from flask import Flask, render_template
import arduino_serial_led as led
import time

app = Flask(__name__)

SERIAL_PORT = "/dev/ttyACM0"
BIT_RATE = 9600

arduino_serial = led.initialize(SERIAL_PORT, BIT_RATE)
time.sleep(2)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enable")
def enable():
    led.control_arduino_led(arduino_serial, "1")
    return render_template("index.html")

@app.route("/disable")
def disable():
    led.control_arduino_led(arduino_serial, "0")
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80")
