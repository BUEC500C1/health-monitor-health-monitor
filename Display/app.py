from flask import Flask, render_template
from database import createBPtable
from database import createO2table
from database import createPulsetable
from database import getBPdata
from database import getO2data
from database import getPulsedata

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