from flask import Flask, render_template
from Display.database import createBPtable
from Display.database import createO2table
from Display.database import createPulsetable
from Display.database import getBPdata
from Display.database import getO2data
from Display.database import getPulsedata

app = Flask(__name__)

@app.route("/")
def main():

    # Creates database tables
    createO2table()
    createBPtable()
    createPulsetable()

    # Gets most recent values from database
    oxygen = getO2data()
    blood_pressure = getBPdata()
    pulse = getPulsedata()

    return render_template("display.html", oxygen=oxygen, bp=blood_pressure, pulse=pulse)  


if __name__ == "__main__":
    app.run(debug=True)