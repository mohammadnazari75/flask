from os import environ

class Config:
    DEBUG = bool(environ.get("AUTHZ_DEBUG", False))
   
    TESTING = bool(environ.get("AUTHZ_TESTING", False))
   
    ENV = environ.get("AUTHZ_ENV", "production")

    SECRET = environ.get("AUTHZ_SECRET", "HARD-DEV-SECRET")
   
    SQLALCHEMY_DATABASE_URI = environ.get("AUTHZ_DATABASE_URI", None)
   
    SQLALCHEMY_ECHO = DEBUG # Logs of db when we are in debug mode
   
    SQLALCHEMY_TRACK_MODIFICATION = DEBUG

    JWT_TOKEN_LIFETIME = int(environ.get("AUTHZ_JWT_TOKEN_LIFETIME", 100))

    JWT_ALGO = environ.get("AUTHZ_JWT_ALGO", "HS512")