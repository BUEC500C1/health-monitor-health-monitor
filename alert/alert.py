from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class alert(Resource):
    def get(self):
        return {"alert": "module"}

api.add_resource(alert, '/')

if __name__ == '__main__':
    app.run()
