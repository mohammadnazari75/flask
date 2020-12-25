from flask import abort,request

from authz import db
from authz.model import User
from authz.schema.apiv1 import UserSchema

class UserController:
    
    def get_users():
        users = User.query.all()
        users_schema = UserSchema(many=True)
        return users_schema.dump(users)
    
    def get_user(user_id):
        user = User.query.get(user_id)
        user_schema = UserSchema()
        if user is None:
            abort(404)
        return user_schema.dump(user)

    def create_user():
        user_schema = UserSchema()
        data = user_schema.load(request.get_json())
        if "username" in data and "password" in data:
            user = User.query.filter_by(username=data["username"]).first()
            if user is None:
                user = User(username=data["username"], password=data["password"])
                db.session.add(user)
                try:
                    db.session.commit()
                except:
                    db.session.rollback()
                    abort(500)
                return user_schema.dump(user)
            else:
                abort(409)
        else:
            abort(400)