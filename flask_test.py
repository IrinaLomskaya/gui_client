import random
from asyncore import read

from flask import Flask
from flask_restful import Api, reqparse, Resource
import json

app = Flask(__name__)
api = Api(app)





with open('ToServer.json') as file:
    templates = json.load(file)


class Quote(Resource):

    def get(self):
        return templates

    def put(self):
        kk = templates[0]['x0']
        print(kk)
        return int(kk) + 3




api.add_resource(Quote, "/api/flask_test")
if __name__ == '__main__':
    app.run(debug=True, port=5550, host="127.0.0.1")
