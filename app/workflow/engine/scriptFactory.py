
from functools import partial
import inspect
import importlib
import requests
import os
import pandas as pd
from flask import current_app as app


class ScriptFactory(object):


    def __init__(self, workflowNode, mapper):
        
        self._workflowNode = workflowNode
        self._mapper = mapper

    @classmethod
    def createClazz(clzz, path, name, initValue = None):
        my_module = importlib.import_module(path)
        clazz = getattr(my_module, name)

        instanzz = clazz() if initValue is None else clazz(initValue)

        return instanzz

    def _initDataPool(self):
        basefilename = app.config["BASEFILENAME"]
        dsPool = []
        for node in self._workflowNode:
            nodepath = self._mapper.get(node).value
            filepath = ''.join([basefilename, nodepath])
        
            ds = ScriptFactory.createClazz(
                node.path, node.name, filepath)
            dsPool.append(ds)
        return dsPool





