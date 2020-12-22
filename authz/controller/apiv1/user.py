from flask import abort,request

from authz import db
from authz.model import User

class UserController:
    
    def get_users():
        user = User.query.all()
        return { "users": users }
    
    def get_user(user_id):
        user = User.query.get(user_id)
        if user is None:
            abort(404)
        return { "user": user }

    def create_user():
        data = request.get_json()
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
                return { "user": user }
            else:
                abort(409)
        else:
            abort(400)