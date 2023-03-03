import random
from asyncore import read
import math
from flask import Flask
from flask_restful import Api, reqparse, Resource
import json
from flask import request

app = Flask(__name__)
api = Api(app)


class Quote(Resource):

    def eq(self, V, k):
        return ((V * V) * math.sin(2 * k * (math.pi / 180)) / 10000)

    @app.route("/flask_server", methods=['POST'])
    def post(self):
        data = request.get_data()
        stri = json.loads(data)
        x = float(stri[0]['x'])
        y = float(stri[0]['y'])
        angle_azimuth = round((math.atan(x/y))*(180/math.pi))
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
        print(new_list)
        return new_list


api.add_resource(Quote, "/api/flask_server")
if __name__ == '__main__':
    app.run(debug=True, port=5557, host="192.168.35.35")
