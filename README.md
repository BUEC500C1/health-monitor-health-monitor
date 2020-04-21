# health-monitor-health-monitor


## Description of Modules

### Bood Pressure Module 

The blood pressure module has a function getBP() which returns a python dictionary in the form {'name': 'bp', 'values': [sys, dia]} where sys is a randomly generated systolic blood pressure between 100 and 135 and dia is a randomly generated diastolic reading between 59 and 88. 

### Oxygen Module

The oxygen module has a function get_oxygen() which returns a python dictionary in the form of {"name": "oxygen", "values": data[random.randint(0, 99)]} where data is an array of potential blood oxygen readings that are read from a static text file. 


### Pulse Module

The pulse module has a function get_pulse() which returns a python dictionary in the form of {"name": "pulse", "values": data[random.randint(0, 99)]} where data is an array of potential pulse readings that are read from a static text file. 


### Alert Module

The alert module has a function getAlert() which returns a python dictionary of the form {"oxygen": oxygen, "bp": sysDia, "pulse": pulse, "alert_oxygen": alert_oxygen, "alert_bp": alert_bp, "alert_pulse": alert_pulse}, where oxygen, pulse and blood pressure values are obtained from their respective modules. The alert values (0 for no alert, 1 for alert) for oxygen, pulse, and blood pressure are determined by the alert module as well (this logic is defined in the functions file).


There is an alert for oxygen if the reading is less than 60. There is an alert for blood pressure if the systolic reading is greater than 130 and the diastolic reading is greater than 80. There is an alert for the pulse if the reading is above 80. 

### Display 

The display module is run as the app.py file. It renders a general display template with the oxygen, blood pressure, and pulse readings as well as any alerts if the are present. 


### AI Module
AI Module uses existed data from database to predict next Blood Pressure, Pulse and Oxygen data. The strategy is to calculate average value. The input or output is as follows
 - Input:  List of origin data, Type(only needed for Blood Pressure)
 - Output:  List of predicted data

## General Flow of Information:

The display (run in the app.py file) periodially requests alerts from the alert module. The alert module then requests readings from the oxygen, blood pressure, and pulse modules and checks for any abnormalities. The alert module then responds with an alert and the display displays the data. 

## How to Run: 

Simply run python3 app.py in the main folder 








