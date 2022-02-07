# -*- coding: utf-8 -*-
from flask_cors import CORS, cross_origin
from flask import Flask, request
from flask_restx import Api, Resource, Namespace, resource
import pickle, json
import pandas as pd
from infos import Infos


app = Flask(__name__)
api = Api(
    app,
    version="1.0",
    title="predict time's API Server",
    description="JYD bigdata API Server",
    terms_url="/",
    contact="87jy1015@gmail.com",
    license="yd networks",
)  # Flask 객체에 api 객체 등록

# api.add_namespace(Infos, "/api")
infos = {}


@api.route("/api")
class inputInfos(Resource):
    def post(self):

        """API 활용하기 위해 조건들 입력 후 예상소요시간 산출 및 제공"""

        with open(
            "/Users/jeyongkim/Dropbox/JYD/datasForAnalyzing/resultTotalBigdata_v1.cpkl",
            "rb",
        ) as f:
            clf = pickle.load(f)

        global infos

        shipping = 0
        carrier = 1
        day1 = 2
        destination = 3
        arrival_time = 4
        day2 = 5

        infos[shipping] = request.json.get("shipping")
        infos[carrier] = request.json.get("carrier")
        infos[day1] = request.json.get("day1")
        infos[destination] = request.json.get("destination")
        infos[arrival_time] = request.json.get("arrival_time")
        infos[day2] = request.json.get("day2")

        a = infos[shipping]
        b = infos[carrier]
        c = infos[day1]
        d = infos[arrival_time]
        e = infos[destination]
        f = infos[day2]

        X = [a, b, c, d, e, f]
        print(X)
        sample = pd.DataFrame(
            [X],
            columns=[
                "shipping",
                "carrier",
                "day1",
                "arrival_time",
                "destination",
                "day2",
            ],
        )
        prediction_day2 = clf.predict(sample)  # 테스트용 값 산출
        print("Predicted:", len(prediction_day2))
        y = str(prediction_day2)
        print(y)
        day = y[1:-3]
        print(day)
        slot = y[-3:-1]
        print(slot)
        if slot == "25":
            hours = "0~6"
        elif slot == "50":
            hours = "6~12"
        elif slot == "75":
            hours = "12~18"
        elif a == "0" and slot == "90":
            hours = "18~24"
        elif a == "1" and slot == "90":
            hours = "16~24"
        elif slot == "30":
            hours = "0~8"
        elif slot == "60":
            hours = "8~16"
        else:
            hours = "16~24"
        interval = f"{day}일 뒤, {hours}시 사이"
        print(interval)
        return interval


CORS(app, resources={r"*": {"origins": "*"}})

if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0")
