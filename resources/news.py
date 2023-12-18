from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
import requests
from config import Config
from mysql_connection import get_connection
from mysql.connector import Error

class NewsSearchResource(Resource) :
    def get(self) : 

        query = request.args.get("query")
        display = request.args.get("display")
        sort = request.args.get("sort")

        url = f"https://openapi.naver.com/v1/search/news.json?query={query}&display={display}&sort={sort}"

        req_header = {"X-Naver-Client-Id" : Config.NAVER_CLIENT_ID,
                      "X-Naver-Client-Secret" : Config.NAVER_CLIENT_SECRET}

        response = requests.get(url, headers=req_header)

        response = response.json()

        return {"result" : "success", "items" : response["items"], "count" : len(response["items"])}, 200
