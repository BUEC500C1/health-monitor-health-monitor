import random

class alert_module():

    def __init__(self):
        pass

    def get_oxygen(self):
        oxy = random.randint(50, 100) #normal oxygen levels are between 75mmHg and 100mmHg
        if oxy < 60: #values under 60mmHg indicate the need for oxygen supply
            err = self.display()
            if err == -1:
                print("Error calling the display")
        return oxy

    def get_bp(self):
        sys = random.randint(100, 140) #normal systolic mmHg is less than 120mmHg
        dia = random.randint(60, 100) #normal diastolic mmHg is lass than 80mmHg
        if sys > 130 or dia > 80: #if systolic or diastolic become high, send alert to the display
            err = self.display()
            if err == -1:
                print("Error calling the display")
        bp = [sys, dia]
        return bp

    def get_pulse(self):
        pulse = random.randint(50, 100) #normal pulse rate is < 80
        if pulse > 80: #if pulse rate is high, send alert to display
            err = self.display()
            if err == -1:
                print("Error calling the display")
        return pulse

    def display(self):
        guess = random.randint(0, 10)
        if guess % 2 == 0:
            return 1
        else:
            return -1
