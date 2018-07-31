from functools import wraps
import inspect
import pandas as pd

# basecase
"""

{
  "workflow":[{
    "id": "1",
    "name": "removeDuplicate",
    "path": "scripts.test",
    "paras": {
        "colName":"PRIMARY_ASSET_ID"
        }
},
{
    "id": "2",
    "name": "selectData",
    "path": "scripts.test",
    "paras": {
          "cols":"PRIMARY_ASSET_ID"
        }
}

],
"type":"chain",
"sequenceId":[2, 1]
}

"""

def task(f):
    if 'rst' in inspect.getargspec(f).args:
        raise TypeError('debug argument already defined')

    @wraps(f)
    def wrapper(*args, rst=False, **kwargs):
        if rst:
            print('Calling', f.__name__)
        return f(*args, **kwargs)
    return wrapper

# @task
class Add():

	def __init__(self):
		pass

	def execute(self, a, b): 
		return a + b


# @task
class Minus():

	def __init__(self):
		pass

	def execute(self, a, b):
		
		return a - b

# @task


class Test():

	def __init__(self):
		pass

	def execute(self, a, b):
		return a - b


class Script(object):

	def __init__(self):
		pass

	def execute(self, a, b):
		return a - b


class removeDuplicate(Script):
	"""
    @Description: Remove duplicate records based on given columns.
    @param df(dataframe): this is dataframe.
    @param colName(string): this is colName.
    @return (dataframe): this is return type.

	@category other
    """

	def execute(self, df, colName):
		# print("removeDuplicate data performing!")
		keepRestData = True
		if colName and keepRestData:	
			df =df.drop_duplicates(colName, inplace=False)
		elif colName and keepRestData == False:
			df = df.drop_duplicates(colName, inplace=False).query(','.join(colName))
		else:
			df = df.drop_duplicates(inplace=False)
			# return df
		return df


class selectData(Script):

	def execute(self, df, cols):
		# print("select data performing!")
		conditionStr = None

		if cols:
			if type(cols) == type('str'):
				return df[[cols]]
			else:
				return df[cols]
		elif conditionStr:
			return (df.query(conditionStr))
		else:
			
			return (df)


class dataDifference(Script):
	"""
	Description:
	This function is used to get the difference of the data.

	:param sourceData: a dict of data frames
	:param on: label or a list of label
				Column or index level names to join on. These must be found in both DataFrames.
				If on is None and not merging on indexes then this defaults to the intersection of the columns in both DataFrames.
	:return: The data frame(s), each work sheet is respect to a data format
	"""

	def execute(self, df, df2):
		on = None

		left_on = ['PRIMARY_ASSET_ID1']
		right_on = ['PRIMARY_ASSET_ID']
		
		df = pd.merge(df, df2, 'outer', on, left_on, 
		              right_on, indicator=True)
		df = df.query('_merge != "both"')
		return (df)


class loadingDatasource01(Script):
	
	def __init__(self, fileName):
		self.fileName = fileName

	def execute(self):
		delimiter = ','
		path = ''
		# Check file extension of the file
		if self.fileName.endswith(('.xlsx', '.xls', '.xlsm')):
			df = pd.read_excel(path + self.fileName, sheet_name=None)
			if len(df.keys()) == 1:
				data = df[list(df.keys())[0]]
				return data
			else:
				return df
		elif self.fileName.endswith('.csv'):
			df = pd.read_csv(path, delimiter)
			return df
		else:
			with open(self.fileName) as f:
				data = f.readlines()
				return data


class loadingDatasource02(Script):

	def __init__(self, fileName):
		self.fileName = fileName

	def execute(self):

		delimiter = ','
		path = ''
		# Check file extension of the file
		if self.fileName.endswith(('.xlsx', '.xls', '.xlsm')):
			df = pd.read_excel(path + self.fileName, sheet_name=None)
			if len(df.keys()) == 1:
				data = df[list(df.keys())[0]]
				return data
			else:
				return df
		elif self.fileName.endswith('.csv'):
			df = pd.read_csv(path, delimiter)
			return df
		else:
			with open(self.fileName) as f:
				data = f.readlines()
				return data


