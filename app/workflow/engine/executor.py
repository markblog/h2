from app.workflow.engine.parser import Parser
from app.workflow.engine.workflow import Workflow
from app.workflow.engine.scriptFactory import ScriptFactory
from flask import current_app as app



class Executor(object):
    
    def __init__(self, data):
        self.data = data

    def executor(self):

        parser = Parser(self.data)
        workflownode, db_pool = parser.parser()
        mapper = parser._mapper_paraNode_with_workflowNode()
        sf = ScriptFactory(db_pool, mapper)
        datasources = sf._initDataPool()

        #run
        wf = Workflow(datasources, workflownode)
        rst = wf.run()
        return rst

    def datasourceExecutor(self):
        print(self.data)
        print(self.data.get("name"))
        print(self.data.get("path"))
        print(self.data.get("paras")[0].value)
        
        return None









        

    
