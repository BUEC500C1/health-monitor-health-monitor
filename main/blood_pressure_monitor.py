import random
import json


def getBP():
    sys = random.randint(100, 135)
    dia = random.randint(59, 88)
    reading = {'name': 'bp', 'values': [sys, dia]}
    return reading
