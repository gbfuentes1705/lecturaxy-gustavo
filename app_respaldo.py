from flask import Flask, render_template
import random

app = Flask(__name__)

def leer_sensor():
    ejeX = round(random.uniform(-1, 1), 2)
    ejeY = round(random.uniform(-1, 1), 2)
    return ejeX, ejeY

@app.route("/")
def index():
    ejeX, ejeY = leer_sensor()
    return render_template("index.html", ejeX=ejeX, ejeY=ejeY)

@app.route("/radar")
def radar():
    ejeX, ejeY = leer_sensor()
    return render_template("radar.html", ejeX=ejeX, ejeY=ejeY)

@app.route("/joystick")
def joystick():
    ejeX, ejeY = leer_sensor()
    return render_template("joystick.html", ejeX=ejeX, ejeY=ejeY)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
