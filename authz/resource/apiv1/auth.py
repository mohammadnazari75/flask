from flask_restx import Resource

from authz.controller.apiv1 import AuthController

class AuthResource(Resource):
    def get(self):
        """
        GET /auth/tokens --> Verify JWT token
        """
        return AuthController.verify_token()

    def post(self):
        """
        POST /auth/token --> Create new JWT token
        """
        return AuthController.create_token()