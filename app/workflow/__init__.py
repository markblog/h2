from flask import Flask, Blueprint
from flask_restful import Api
from . import resource as WorkflowResource
from flask import current_app

workflow_bp = Blueprint('workflow', __name__)

api = Api(workflow_bp, prefix='/api/v1')

api.add_resource(WorkflowResource.WorkflowListResource, '/workflows') # post a workflow
api.add_resource(WorkflowResource.ScriptsListResource, '/scripts')
api.add_resource(WorkflowResource.DatasourcesListResource, '/datasources/<id>')  # 4 , 5 is datasource key in the text case
# api.add_resource(UserResource.LoginResource, '/users/login')
