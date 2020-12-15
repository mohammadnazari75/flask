from os import environ

class Config:
    DEBUG = bool(environ.get("AUTHZ_DEBUG", False))
    TESTING = bool(environ.get("AUTHZ_TESTING", False))
    ENV = environ.get("AUTHZ_ENV", "production")