from flask import Flask
from flask_restful import Resource, Api

import functions as f

app = Flask(__name__)
api = Api(app)

class alert(Resource):
    def get(self):
        alert = f.alert_module()

        oxygen = alert.get_oxygen()
        sysDia = alert.get_bp()
        pulse = alert.get_pulse()
        
        bp = str(sysDia[0]) + "/" + str(sysDia[1])

        return {"oxygen": oxygen, "blood pressure": bp, "pulse": pulse}

api.add_resource(alert, '/')

if __name__ == '__main__':
    app.run(debug=True)
