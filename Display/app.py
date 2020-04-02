from flask import Flask, render_template
import database as db 

app = Flask(__name__)

@app.route("/")
def main():

    # Gets most recent values from database
    oxygen = getO2data()
    blood_pressure = getBPdata()
    pulse = getPulsedata()
    return render_template("display.html", oxygen=oxygen, bp=blood_pressure, pulse=pulse);   


if __name__ == "__main__":
    app.run(debug=True)