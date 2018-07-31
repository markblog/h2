from app.workflow.engine.validator import Validator
from app.workflow.engine.workflow import WorkflowNode
from app.workflow.engine.workflow import ParaNode

class Parser(object):

    def __init__(self, data):
        self.data = data
        self.workflowNodes = []
        self.paraNodes = []
        self.named_workflowNode = {}
        self.dbpool = []

    def dataChecker(self, data):
        if not Validator.existAndNotNone(['workflow'], self.data):
            raise "missing workflow parameter in the data"

    def _workflownodesParser(self):
        _names =[]
        for item in self.data.get('workflow'):
            workflowNode = WorkflowNode.from_dict(item)
            _names.append(workflowNode.name)
            self.workflowNodes.append(workflowNode)
        self.named_workflowNode = dict(zip(_names, self.workflowNodes))


    def _paranodeParser(self):
        for i in range(len(self.workflowNodes)):
            for j in range(len(self.workflowNodes[i].paras)):
                paraNode = ParaNode.from_dict(self.workflowNodes[i].paras[j])
                self.paraNodes.append(paraNode)

    def _mapper_paraNode_with_workflowNode(self):
        return dict(zip(self.workflowNodes, self.paraNodes))

        

    
    def _dbpool(self):
        self.dbpool = [self.named_workflowNode.get(
            paranode.value) for paranode in self.paraNodes if paranode.para_type == "func_key" and paranode.value[:-2] == "loadingDatasource"]

   
    def parser(self):
        self._workflownodesParser()
        self._paranodeParser()
        self._dbpool()
        return self.workflowNodes, self.dbpool
        # print(self.dbpool[0].name)
        



