from os import environ

class Config:
    DEBUG = bool(environ.get("AUTHZ_DEBUG", False))
   
    TESTING = bool(environ.get("AUTHZ_TESTING", False))
   
    ENV = environ.get("AUTHZ_ENV", "production")
   
    SQLALCHEMY_DATABASE_URI = environ.get("AUTHZ_DATABASE_URI", None)
   
    SQLALCHEMY_ECHO = DEBUG # Logs of db when we are in debug mode
   
    SQLALCHEMY_TRACK_MODIFICATION = DEBUG