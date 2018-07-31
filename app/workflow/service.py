import json
from app.workflow.model import Script
import importlib
from flask import current_app as app


fileMapper = {"loadingDatasource01": "app\\datasource\\export_OSR_20180228.xlsx",
              "loadingDatasource02": "app\\datasource\\export_FLX_20180228.xlsx"}

def datasourceLoading(id):
    basefilename = app.config["BASEFILENAME"]
    rs = Script.query.filter_by(id=id).first()
    js = json.loads(json.dumps(rs.to_dict()))
    path = js.get("path", None)
    name = js.get("name", None)
    filepath = fileMapper.get(name, None)
    filepath = ''.join([basefilename, filepath])
    my_module = importlib.import_module(path)
    clazz = getattr(my_module, name)
    instanzz = clazz(filepath)

    rst = instanzz.execute()
    datasource = list(rst['Export Worksheet'].columns.values)
    return datasource


def load_data():
    script01 = Script(id=1,
                      name='selectData',
                      path='scripts.test',
                      r_type="Dataframe",
                      paras=json.dumps([
                          {"name": "cols",
                             "type": "String"
                           },
                          {"name": "df",
                           "type": "Dataframe"
                           }
                      ]),
                      description="Select columns from data based on conditions"
                      )
    script02 = Script(id=2,
                      name='removeDuplicate',
                      path='scripts.test',
                      r_type="Dataframe",
                      paras=json.dumps([
                          {"name": "colName",
                             "type": "String"
                           },
                          {"name": "df",
                           "type": "Dataframe"
                           }]),
                      description="Remove duplicate records based on given columns."
                      )
    script03 = Script(id=3,
                      name='dataDifference',
                      path='scripts.test',
                      r_type="Dataframe",
                      paras=json.dumps([
                          {"name": "df",
                           "type": "Dataframe"
                           },
                          {"name": "df2",
                           "type": "Dataframe"
                           }]),
                      description="This function is used to get the difference of the data.")

    script04 = Script(id=4,
                      name='loadingDatasource01',
                      path='scripts.test',
                      r_type="Dataframe",
                      paras=json.dumps([
                          {
                              "name": "filePath",
                              "type": "String"
                          }
                      ]),
                      description="loading data source")
    script05 = Script(id=5,
                      name='loadingDatasource02',
                      path='scripts.test',
                      r_type="Dataframe",
                      paras=json.dumps([
                          {
                              "name": "filePath",
                              "type": "String"
                          }
                      ]),
                      description="loading data source")

    db.session.add_all([script01, script02, script03, script04, script05])
    db.session.flush()
