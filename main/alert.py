import functions as f

def getAlert():
    alert = f.alert_module()

    oxygen = alert.get_oxygen()
    sysDia = alert.get_bp()
    pulse = alert.get_pulse()
    
    err = alert.database({"oxygen": oxygen, "bp": sysDia, "pulse": pulse})

    alert_oxygen = alert.get_oxygen_alert(oxygen)

    alert_bp = alert.get_blood_pressure_alert(sysDia)

    alert_pulse = alert.get_pulse_alert(pulse)


    return {"oxygen": oxygen, "bp": sysDia, "pulse": pulse, "alert_oxygen": alert_oxygen, "alert_bp": alert_bp, "alert_pulse": alert_pulse}


if __name__ == "__main__":
    print(getAlert().items())
