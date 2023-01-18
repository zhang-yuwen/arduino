from flask import Flask, render_template, redirect
from arduino import LED
from time import sleep

led=LED()

app = Flask(__name__)

@app.route("/")
def status():
    print(f'Led state: {led.led_state}')
    if led.led_state:
        return render_template('index.html', message = "LED lights are on.")
    else:
        return render_template('index.html', message = "LED lights are off.")

@app.route("/on", methods = ['POST'])
def on():
    led.on()
    sleep(0.1)
    return redirect("/", code=302)


@app.route("/off", methods = ['POST'])
def off():
    led.off()
    sleep(0.1)
    return redirect("/", code=302)

# flask --app web.py run --port 8080
# ngrok http 8080 