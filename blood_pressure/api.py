from flask import Flask
import blood_pressure_monitor as bpm
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class bloodpressure(Resource):
    def get(self):
        return bpm.getBP()


api.add_resource(bloodpressure, '/getbp/')

if __name__ == '__main__':
    app.run(debug=True)
