import random
from asyncore import read
import math
from flask import Flask
from flask_restful import Api, reqparse, Resource
import json

app = Flask(__name__)
api = Api(app)

def op():
    with open('ToServer.json') as file:
        templates = json.load(file)
    return templates

def op_g():
    with open('ToServer_g.json') as file:
        templates2 = json.load(file)
    return templates2
class Quote(Resource):

    def get(self):
        return op()

    def eq(self, V, k):
        return ((V * V) * math.sin(2 * k * (math.pi / 180)) / 10000)

    def put(self):
        x = int(op()[0]['x'])
        y = int(op()[0]['y'])
        angle_azimuth = (math.atan(x/y))*(180/math.pi)
        print(angle_azimuth)
        r = math.sqrt(x * x + y * y)
        aV = []
        aK = []

        def eq(V, k):
            return ((V * V) * math.sin(2 * k * (math.pi / 180)) / 10000)

        for V in range(100, 1000, 100):
            for k in range(1, 89):
                if abs(eq(V, k) - r) < 0.1:
                    aV.insert(V, k)
                    aK.insert(k, V)
        V = aV[0]
        k = aK[0]
        new_list = [{"azimuth": int(angle_azimuth), "elevation": int(V), "speed": int(k)}]
        def wr():
            with open('ToClientSolved.json', 'w') as file_json:
                file_new = json.dumps(new_list, indent=4)
                file_json.write(file_new)
            return file_new
        return wr()



api.add_resource(Quote, "/api/flask_test")
if __name__ == '__main__':
    app.run(debug=True, port=5550, host="127.0.0.1")
