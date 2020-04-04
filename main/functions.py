import random

from blood_pressure_monitor import getBP
from oxygen import get_oxygen
from pulse import get_pulse

class alert_module():

    def __init__(self):
        pass

    def get_oxygen(self):
        oxy = int(get_oxygen()["values"])
        # if oxy < 60: #values under 60mmHg indicate the need for oxygen supply
        #     err = self.display()
        #     if err == -1:
        #         print("Error calling the display")
        return oxy

    def get_bp(self):
        reading = getBP()
        sys = reading["values"][0] #normal systolic mmHg is less than 120mmHg
        dia = reading["values"][1] #normal diastolic mmHg is lass than 80mmHg
        # if sys > 130 or dia > 80: #if systolic or diastolic become high, send alert to the display
        #     err = self.display()
        #     if err == -1:
        #         print("Error calling the display")
        bp = [sys, dia]
        return bp

    def get_pulse(self):
        pulse = get_pulse()['values']
        # if pulse > 80: #if pulse rate is high, send alert to display
        #     err = self.display()
        #     if err == -1:
        #         print("Error calling the display")
        return pulse

    # def display(self):
    #     guess = random.randint(0, 10)
    #     if guess % 2 == 0:
    #         return 1
    #     else:
    #         return -1

    def get_oxygen_alert(self,reading):
        if reading < 60:
            return 1
        else:
            return 0

    def get_blood_pressure_alert(self,reading):
        if reading[0] > 130 or reading[1] > 80:
            return 1
        else:
            return 0
    def get_pulse_alert(self,reading):
        if reading > 80:
            return 1
        else:
            return 0

    def database(self, oxygen, systolic, diastolic, pulse):
        print("data sent to the database")
        return 1
