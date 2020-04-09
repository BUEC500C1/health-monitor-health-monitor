from flask import Flask, render_template
from Database.database import getO2data, getBPdata, getPulsedata
from alert import getAlert
from AI import AI_analysis

app = Flask(__name__)

oxygen_array = []
bp_array = []
pulse_array = []
o2_predicted = []
bp_predicted = []
pulse_predicted = []

@app.route("/")
def main():
    alert = getAlert()
    oxygen = alert['oxygen']
    blood_pressure = alert['bp']
    pulse = alert['pulse']

    if len(oxygen_array) > 0:
        oxygen_array.append(oxygen)
        bp_array.append(blood_pressure)
        pulse_array.append(pulse)
    else:  
        oxygen_str = getO2data()
        bp_str = getBPdata()
        pulse_str = getPulsedata()
        num = 0
        if(len(oxygen_str) > 10):
            num = len(oxygen_str) - 10
        for i in range(num, len(oxygen_str)):
            oxygen_array.append(oxygen_str[i])
            bp_array.append(bp_str[i].split())
            pulse_array.append(pulse_str[i])

    while(len(oxygen_array) > 10):
        oxygen_array.pop(0)
        bp_array.pop(0)
        pulse_array.pop(0)
        
    #add predicted value     
    o2_predicted = AI_analysis(oxygen_array)
    bp_predicted = AI_analysis(bp_array, "bp")
    pulse_predicted = AI_analysis(pulse_array)
    
    
    return render_template("display.html", 
        oxygen=oxygen_array, 
        bp=bp_array,
        pulse=pulse_array, 
        o2predicted = o2_predicted,
        bppredicted = bp_predicted,
        pulsepredicted = pulse_predicted,
        oxygen_alert=alert['alert_oxygen'],
        bp_alert=alert['alert_bp'], 
        pulse_alert=alert['alert_pulse'], 
        len=(len(oxygen_array)))  

if __name__ == "__main__":
    app.run(debug=True)