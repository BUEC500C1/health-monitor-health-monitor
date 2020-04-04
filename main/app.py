from flask import Flask, render_template
from Display.database import createBPtable
from Display.database import createO2table
from Display.database import createPulsetable
from Display.database import getBPdata
from Display.database import getO2data
from Display.database import getPulsedata


from alert import getAlert
from timer import timer

app = Flask(__name__)

@app.route("/")
def main():
    
    # # Creates database tables
    # createO2table()
    # createBPtable()
    # createPulsetable()

    # Gets most recent values from alert
    alert = getAlert()
    oxygen = alert['oxygen']
    blood_pressure = alert['bp']
    pulse = alert['pulse']

    if alert['alert_oxygen'] == 1:
        return render_template("oxy_alert.html", oxygen=oxygen, bp_sys=blood_pressure[0],bp_dia=blood_pressure[1], pulse=pulse)
    if alert['alert_bp'] == 1:
        return render_template("bp_alert.html", oxygen=oxygen,bp_sys=blood_pressure[0],bp_dia=blood_pressure[1], pulse=pulse)

    if alert['alert_pulse'] == 1:
        return render_template("pulse_alert.html", oxygen=oxygen,bp_sys=blood_pressure[0],bp_dia=blood_pressure[1], pulse=pulse)

    return render_template("display.html", oxygen=oxygen, bp_sys=blood_pressure[0],bp_dia=blood_pressure[1], pulse=pulse)  




if __name__ == "__main__":
    app.run(debug=True)