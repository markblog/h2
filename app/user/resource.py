# from utils.patch import BasicResource
from flask_restful import Resource

from flask import request, g
from app.ext import db, redis_db
# from utils.decorators import auth
# from app.services import user_services

class WorkflowListResource(Resource):
    """docstring for WorkflowListResource"""
    def get(self):
        return 'user created success', 201


class WorklflowResource(Resource):
    """docstring for WorklflowResource"""
    def post(self):
        
        pass
