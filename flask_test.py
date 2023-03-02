import random
from asyncore import read

from flask import Flask
from flask_restful import Api, reqparse, Resource
import json

app = Flask(__name__)
api = Api(app)

def op():
    with open('ToServer.json') as file:
        templates = json.load(file)
    return templates

class Quote(Resource):

    def get(self):
        return op()

    def put(self):
        kk = op()[0]['x0']
        print(kk)
        return int(kk) + 3

    def delete(self):
        return templates


api.add_resource(Quote, "/api/flask_test")
if __name__ == '__main__':
    app.run(debug=True, port=5550, host="127.0.0.1")
