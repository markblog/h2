import inspect
from utils.mixins import DictMixin
from collections import defaultdict
from app.workflow.engine.scriptFactory import ScriptFactory
from collections import OrderedDict
import os
from pathlib import Path

class WorkflowNode(DictMixin):

	id = 'id'
	name = 'name'
	path = 'path'
	paras = 'paras'


class ParaNode(DictMixin):

	name = 'name'
	value = 'value'
	para_type = 'para_type'
	

class Workflow():
	def __init__(self, dbpool, workflowNodeList):
		self.dbpool = dbpool
		self.workflowNodeList = workflowNodeList
		self.result = OrderedDict()
		# self.dataHolder = {}

	def run(self):
		#init pool
		for data in self.dbpool:
			value = data.execute()
			value = value['Export Worksheet']
			self.result[data.__class__.__name__] = value
		if self.workflowNodeList is None:
			print("sssssssssssssssssss")
			return self.result
		#run workflow
		for workflownode in self.workflowNodeList:
			if workflownode.name not in self.result.keys():
				for i in workflownode.paras:
					if i.get("para_type") == "func_key" and i.get("value")[:-2] == "loadingDatasource":
						i["value"] = self.result[i.get("value")]
		twd = []
		for workflownode in self.workflowNodeList:
			wf_dict = {}
			if workflownode.name not in self.result.keys():
				for i in workflownode.paras:
					wf_dict[i['name']] = i["value"]
				twd.append(wf_dict)

		removeNodeList = []
		for workflownode in self.workflowNodeList:
			if workflownode.name in self.result.keys():
				removeNodeList.append(workflownode)
		self.workflowNodeList = [
			x for x in self.workflowNodeList if x not in removeNodeList]


		callableNodePair = OrderedDict(zip(self.workflowNodeList, twd))

		for ds, v in callableNodePair.items():
			print(self.result.keys())
			if isinstance(v.get("df"), str):
				v['df'] = self.result[v.get("df")]

			if isinstance(v.get("df2"), str):
				v['df2'] = self.result[v.get("df2")]

			if ds.name[:-2] == "loadingDatasource":
				continue

			ds = ScriptFactory.createClazz(ds.path, ds.name)
			rst = ds.execute(**v)
			rstKey = ds.__class__.__name__
			if rstKey not in self.result:
				self.result[rstKey] = rst

		index = 0
		for k, v in self.result.items():
			# if k[:-2] == "loadingDatasource":
			# 	continue
			# else:
			dir_path = os.path.dirname(os.path.realpath(__file__))
			rstPath = Path(dir_path).parent.parent.parent
			index += 1
			filepath = 'test_suite/result/'+'workflow_1_step'+str(index)+'.csv'
			if os.path.exists(filepath):
			    filepath = 'test_suite/result/'+'workflow_2_step'+str(index)+'.csv'
			csv_name = rstPath.joinpath(filepath)
			v.to_csv(csv_name)
			rst.append(v)
		return self.result[next(reversed(self.result))]








