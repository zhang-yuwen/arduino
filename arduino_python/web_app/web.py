from flask import Flask, render_template, redirect
from serial_money import serial_io, control, led_state, led_on, led_off
import threading
from time import sleep

thread1 = threading.Thread(target=serial_io)
thread2 = threading.Thread(target=control)

thread1.start()
# thread2.start()

app = Flask(__name__)

@app.route("/")
def status():
    print(f'Led state: {led_state}')
    if led_state:
        return render_template('index.html', message = led_state[-1])
    else:
        return render_template('index.html', message = "empty")
    #return led_state[-1]

@app.route("/on", methods = ['POST'])
def on():
    led_on()
    sleep(0.1)
    return redirect("/", code=302)


@app.route("/off", methods = ['POST'])
def off():
    led_off()
    sleep(0.1)
    return redirect("/", code=302)

# flask --app web_app/web.py run --port 8080
# ngrok http 8080 