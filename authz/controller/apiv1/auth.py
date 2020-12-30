from time import time
from jwt import encode, decode
from flask import abort, request
from jwt.exceptions import ExpiredSignatureError

from authz.config import Config
from authz.model import User
from authz.schema.apiv1 import UserSchema

class AuthController:

    def create_token():
        if not request.is_json:
            abort(415)
        user_schema = UserSchema()
        data = user_schema.load(request.get_json())
        if "username" in data and "password" in data:
            user = User.query.filter_by(username=data["username"]).first()
            if user is None:
                abort(404)
            if user.password == data["password"]:
                current_time = time()
                jwt_token = encode(
                    {
                        "username": user.username,
                        "user_id": user.id,
                        "iss": "authz",
                        "iat": current_time,
                        "nbf": current_time,
                        "exp": current_time + Config.JWT_TOKEN_LIFETIME
                    },
                    Config.SECRET,
                    algorithm=Config.JWT_ALGO
                ).decode('utf8')
                return { "user": user_schema.dump(user) }, 201, { "X-Subject-Token": jwt_token }
            else:
                abort(401)
        else:
            abort(400)


    def verify_token():
        if not request.is_json:
            abort(415)
        if "X-Subject-Token" not in request.headers:
            abort(400)
        jwt_token = request.headers.get("X-Subject-Token")
        try:
            jwt_token_data = decode(
                    jwt_token,
                    Config.SECRET,
                    algorithm=[Config.JWT_ALGO]
            )
        except ExpiredSignatureError:
            abort(401)
        except:
            abort(400)
        user = User.query.get(jwt_token_data["user_id"])
        if user is None:
            abort(404)
        user_schema = UserSchema()
        return { "user": user_schema.dump(user) }, 200, { "X-Subject-Token": jwt_token }