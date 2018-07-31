from flask import Flask, Blueprint
from flask_restful import Api
from . import resource as UserResource
from flask import current_app

user_bp = Blueprint('user', __name__)

api = Api(user_bp, prefix = '/api/v1')

# api.add_resource(UserResource.UserListResource, '/users')
# api.add_resource(UserResource.LoginResource, '/users/login')



