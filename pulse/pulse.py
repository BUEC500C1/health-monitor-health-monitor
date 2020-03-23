import array
import random
import json
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


def read_file():
    file = open("pulse_data.txt", "r")
    data = array.array('i', [])
    for line in file:
        data.append(int(line))
    return data


def get_pulse():
    data = read_file()
    data_set = {"name": "pulse", "values": []}
    json_dump = json.dumps(data_set)
    json_object = json.loads(json_dump)
    json_object["values"].append(data[random.randint(0, 99)])
    return json_object


class pulse(Resource):
    def get(self):
        return get_pulse()


api.add_resource(pulse, '/')

if __name__ == '__main__':
    app.run(debug=True)
