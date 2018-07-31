from flask import request
from app.tests.model import Test
from app.workflow.engine.executor import Executor
from flask import render_template
from flask_restful import Resource
from app.workflow.model import Script
from app.ext import db
import json
from flask import jsonify
from flask import current_app as app
import importlib
from app.workflow.service import datasourceLoading
from app.workflow.service import load_data

"""

 ________________________________version7____________________________
 #post request
{
  "workflow":[
    {
     "id": "101",
     "name": "loadingDatasource01",
     "path": "scripts.test",
     "paras": [
     {
         "name":"filePath",
         "value": "app\\datasource\\export_OSR_20180228.xlsx",
         "para_type": "key"
         }
     ]}
    ,
     {
     "id": "101",
     "name": "loadingDatasource02",
     "path": "scripts.test",
     "paras": [
     {
         "name":"filePath",
         "value": "app\\datasource\\export_FLX_20180228.xlsx",
         "para_type": "key"
         }
     ]}
    ,
     {
     
 "id": "1",
    "name": "selectData",
    "path": "scripts.test",
    "paras": [
      {"name": "cols",
      "value": "PRIMARY_ASSET_ID",
      "para_type": "key"
      },
      {"name": "df",
       "value": "loadingDatasource01",
       "para_type": "func_key"

      }]
      },
      {
    "id": "1",
    "name": "removeDuplicate",
    "path": "scripts.test",
    "paras": [
      {"name": "colName",
      "value": "PRIMARY_ASSET_ID",
      "para_type": "key"
      },
      {"name": "df",
       "value": "selectData",
       "para_type": "func_key"
      }]
      },
      {
     "id": "1",
    "name": "dataDifference",
    "path": "scripts.test",
    "paras": [
      {"name": "df",
      "value": "loadingDatasource02",
      "para_type": "func_key"
      },
      {"name": "df2",
       "value": "loadingDatasource01",
       "para_type": "func_key"
      }]
      
      }
      
    ]
}

Content-Type:application/json
http://127.0.0.1:5555/api/v1/workflows
"""      

class WorkflowResource(Resource):

    def get(self):
        return 'this is workflow', 200


class WorkflowListResource(Resource):

    def post(self):
        data = request.get_json()
        gen_data = Executor(data).executor()        
        return json.dumps(gen_data.to_dict(orient='list'))

    def get(self):
        return "test"


class ScriptsListResource(Resource):

  def get(self):
      rs = Script.query.all()
      rst = []
      for i in rs:
          rst.append(i.to_dict())
      return rst

  def post(self):
      load_data()


class DatasourcesListResource(Resource):
  def get(self, id):
      datasource = datasourceLoading(id)
      return datasource

