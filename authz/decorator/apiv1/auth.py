from functools import wraps
from flask import abort, request
from jwt import decode
from jwt.exceptions import ExpiredSignatureError

from authz.model import User
from authz.config import Config

function_role_mapper = {
    "get_users": {
        "users":  ["admin"]
    },
    "get_user": {
        "users": ["admin", ":user_id"]
    }
}


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            abort(415)
        if "X-Auth-Token" not in request.headers:
           abort(401)
        jwt_token = request.headers.get("X-Auth-Token")
        try:
            jwt_token_data = decode(
                jwt_token,
                Config.SECRET,
                algorthm=[Config.JWT_ALGO]
            )
        except ExpiredSignatureError:
            abort(401)
        except:
            abort(401)
        user = User.query.get(jwt_token_data["user_id"])
        if user is None:
            abort(404)
        func_mapper = function_role_mapper[func.__name__] 
        if user.username in func_mapper["users"]:
            return func(*args,**kwargs)
        elif ":user_id" in func_mapper["users"]:
            user_id_mapper = func.__code__.co_varnames.index("user_id")
            if args[user_id_mapper] == user.id:
                return func(*args, **kwargs)
            else:
                abort(403)
        else:
            abort(403)
    return wrapper