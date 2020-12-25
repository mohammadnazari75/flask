from flask import Flask,Blueprint
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

from authz.config import Config # Import application config.

db = SQLAlchemy()
mg = Migrate()
ma = Marshmallow()

apiv1_bp = Blueprint("apiv1", __name__, url_prefix="/api/v1") # Create /api/v1 endpoint.
apiv1 = Api(apiv1_bp) # Create API for /api/v1 endpoint.

from authz import resource

def create_app():
    app = Flask(__name__) # Create application instance.
    app.config.from_object(Config) # Set application configuration.
    db.init_app(app) # Initialize db with app configuration
    mg.init_app(app, db) # Initialize db migration with app configuration
    ma.init_app(app)
    app.register_blueprint(apiv1_bp) # Register /api/v1 to application.
    return app # Return application instance to caller.