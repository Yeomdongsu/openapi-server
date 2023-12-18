from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from config import Config
from resources.naver import ChineseResource
from resources.news import NewsSearchResource
# 로그아웃 관련된 import문
# from resources.user import jwt_blocklist

# flask 프레임워크를 이용한 Restful API 서버 개발

app = Flask(__name__)

# 환경변수 세팅
app.config.from_object(Config)
# JWT 매니저를 초기화
jwt = JWTManager(app)
# 로그아웃된 토큰으로 요청하면, 실행되지 않게 처리하는 코드
# @jwt.token_in_blocklist_loader
# def check_if_token_is_revoked(jwt_header, jwt_payload) :
#     jti = jwt_payload['jti']
#     return jti in jwt_blocklist

api = Api(app)

api.add_resource(ChineseResource, "/chinese")
api.add_resource(NewsSearchResource, "/news")

if __name__ == "__main__" :
    app.run()