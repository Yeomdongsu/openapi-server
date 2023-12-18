from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
import requests
from config import Config
from mysql_connection import get_connection
from mysql.connector import Error

class ChineseResource(Resource) :

    def post(self) : 

        data = request.get_json()

        # 네이버 파파고 api를 호출해 결과를 가져온다.
        # 파파고 api 문서를 보고, 어떤 데이터를 보내야 하는지 파악하고
        # requests의 get, post, put, delete 등 함수를 이용하여 호출한다.

        req_data = {"source" : "ko", "target" : "zh-CN", "text" : data["sentence"]}

        req_header = {"X-Naver-Client-Id" : Config.NAVER_CLIENT_ID,
                      "X-Naver-Client-Secret" : Config.NAVER_CLIENT_SECRET}

        response = requests.post(url="https://openapi.naver.com/v1/papago/n2mt",
                    data=req_data, headers=req_header)
        
        # 데이터를 받아왔으니 필요한 부분만 뽑아낸다.
        response = response.json()
        
        chinese = response["message"]["result"]["translatedText"]

        return {"result" : "success", "chinese" : chinese}, 200