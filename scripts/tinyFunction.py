import pandas as pd


def loadDataLocally(path, fileName, delimiter = ','):
    """
    Description:
        Load single file(.txt, .csv, .xlsx) from local computer

    :param path: The path of file
    :param fileName: The name of a file
    :param delimiter: The delimiter of the data, this is used when data is .txt or
                    other special format
    :return: The data frame(s), each work sheet is respect to a data format
    """

    # Check file extension of the file
    if fileName.endswith(('.xlsx', '.xls', '.xlsm')):
        df = pd.read_excel(path + fileName, sheet_name=None)
        if len(df.keys()) == 1:
            data = df[list(df.keys())[0]]
            return data
        else:
            return df
    elif fileName.endwith(['.csv']):
        df = pd.read_csv(path, delimiter)
        return df
    else:
        with open(fileName) as f:
            data = f.readlines()
            return data


def selectData(df, cols=None, conditionStr=None):
    """
    Description:
        Select columns from data based on conditions

    :param df: source data 
    :param cols: label or a list of labels, for example 'A', ['A','B']
    :param conditionStr: str 'A>B & A == "aa"'
    :return: The data frame(s), each work sheet is respect to a data format
    """

    if cols:
        if type(cols) == type('str'):
            return df[[cols]]
        else:
            return df[cols]
    elif conditionStr:
        return (df.query(conditionStr))
    else:
        return (df)


def dataInsersaction(df1, df2, on=None, left_on=None, right_on=None):
    """
    Description:
    This function is used to get the inner join of the data.

    :param df1: a data frame
    :param df2: a data frame
    :param on: label or a list of label
                Column or index level names to join on. These must be found in both DataFrames. 
                If on is None and not merging on indexes then this defaults to the intersection of the columns in both DataFrames.
    :return: The data frame(s), each work sheet is respect to a data format 
    """

    df = pd.merge(df1, df2, 'inner', on, left_on, right_on)
    return (df)



def dataDifference(df1, df2, on=None, left_on=None, right_on=None):
    """
    Description:
    This function is used to get the difference of the data.

    :param sourceData: a dict of data frames
    :param on: label or a list of label
                Column or index level names to join on. These must be found in both DataFrames. 
                If on is None and not merging on indexes then this defaults to the intersection of the columns in both DataFrames.
    :return: The data frame(s), each work sheet is respect to a data format 
    """
    df = pd.merge(df1, df2, 'outer', on, left_on, right_on, indicator=True)
    df = df.query('_merge != "both"')
    return (df)



def dataOuterJoin(sourceData, on):
    """
    Description:
    This function is used to get the outer join of the result.

    :param sourceData: a dict of data frames
    :param on: label or a list of label
                Column or index level names to join on. These must be found in both DataFrames. 
                If on is None and not merging on indexes then this defaults to the intersection of the columns in both DataFrames.
    :return: The data frame(s), each work sheet is respect to a data format 
    """
    return (df)


def removeDuplicate(df, colName=None, keepRestData=True):
    """
    Description:
    Remove duplicate records based on given columns.
    
    :param df: 
    :param colName: 
    :param keepRestData:
    :return: 
    """

    if colName and keepRestData:
        df.drop_duplicates(colName, inplace=True)
    elif colName and keepRestData == False:
        df.drop_duplicates(colName, inplace=True).query(','.join(colName))
    else:
        df.drop_duplicates(inplace=True)
    return df


def sortData(df, columnName, ascendingV = True):
    """
    Description:
    Sort data with column name.
    
    :param df: 
    :param columnName: 
    :param ascending: 
    :return: 
    """
    df = df.sort_values(columnName, ascending = ascendingV)

    return df



def filterData(df1, df2, keys=None, mode='interaction'):
    """
    Description:
    Filter data with other dataframes

    :param df1: 
    :param df2: 
    :param keys: 
    :param mode: 
    :return: 
    """
    if keys and mode == 'interaction':
        i1 = df1.set_index(keys).index.astype(str)
        i2 = df2.set_index(keys).index.astype(str)
        return (df1[i1.isin(i2)])
    elif keys and mode == 'difference':
        i1 = df1.set_index(keys).index.astype(str)
        i2 = df2.set_index(keys).index.astype(str)
        return (df1[~i1.isin(i2)])
    elif keys == None and mode == 'interaction':
        return (df1[df1.isin(df2)].astype(str))
    elif keys == None and mode == 'difference':
        return (df1[~df1.isin(df2).astype(str)])
    else:
        return (pd.DataFrame())


def insertColumn(df, colName):
    """
    Description: insert new column in df
    
    :param df: 
    :param colName: 
    :return: 
    """
    df[colName] = ""

    return(df)







'''
#####################################
#test case1 (NEW_GASB_unclass_template)
#####################################

export_FLX = loadDataLocally('C:\\Users\\v627621\\Desktop\\report material\\SearchData\\#61_NEW_GASB_unclass_template_source data\\',
                             'export_FLX_20180228.xlsx')

export_OSR = loadDataLocally('C:\\Users\\v627621\\Desktop\\report material\\SearchData\\#61_NEW_GASB_unclass_template_source data\\',
                             'export_OSR_20180228.xlsx')

# export_OSR = export_OSR['Export Worksheet'].drop_duplicates(['PRIMARY_ASSET_ID'])[['PRIMARY_ASSET_ID']]
export_OSR = removeDuplicate(export_OSR['Export Worksheet'], ['PRIMARY_ASSET_ID'])
export_OSR = selectData(export_OSR, 'PRIMARY_ASSET_ID')

df = dataDifference(export_FLX['Export Worksheet'], export_OSR[['PRIMARY_ASSET_ID']], left_on=['PRIMARY_ASSET_ID1'],
                    right_on=['PRIMARY_ASSET_ID'])
print(df.query('SPONSOR_ID == "CPERS" & XYZ == "331"'))
'''


'''
####################################
#test case2-1 (Corporate Action New Tool-Daily)
#Process 1: Divided fund to the tab. 
#The function of add performanced CA select problem
####################################

BrokeList = loadDataLocally('C:\\Users\\v627621\\Desktop\\report material\\SearchData\\Corporate Action New Tool-Daily\\',
                             'List.xlsx')
Data =  loadDataLocally('C:\\Users\\v627621\\Desktop\\report material\\SearchData\\Corporate Action New Tool-Daily\\',
                             'Data.xlsx')
SecLevel = loadDataLocally('C:\\Users\\v627621\\Desktop\\report material\\SearchData\\Corporate Action New Tool-Daily\\',
                             'SecLevel.xlsx')
SpinOff_Data = loadDataLocally('C:\\Users\\v627621\\Desktop\\report material\\SearchData\\Corporate Action New Tool-Daily\\',
                             'SpinOff Data.xlsx')


BrokerCode = selectData(BrokeList, 'Broker Code')
#print(BrokeList[['Broker Code']])
filteredData = filterData(Data, BrokerCode, ['Broker Code'])
#print(filteredData)
sortedData = sortData(filteredData, ['Fund', 'Trade Date', 'Broker Code', 'Base Net Proceed Amount'])
FundDetailPrevious = insertColumn(sortedData, 'Performed_CA')
Fund_SpinOff_Data = selectData(SpinOff_Data, None, 'Fund == "TC1S"')
#FundDetail = selectData(sortedData, None, 'Fund == "TC1S" and Performed_CA == "Y"')
FundDetail = selectData(sortedData, None, 'Fund == "TC1S"')
print(FundDetail)
'''



'''
####################################
#test case2-2 (Corporate Action New Tool-Daily)
#Process 2: Combine data with sortdata 
####################################

mergedSortedData = dataInsersaction(FundDetail, SecLevel, on=None, left_on=['Fund', 'CUSIP NUMBER'], right_on=['Account ID', 'SSC Security ID'])
partOfMergedSortedData = selectData(mergedSortedData, ['Month To Date ROR', 'Fund', 'Fund Name', 'CUSIP NUMBER', 'Security Name', 'Trade Date', 'Post Date',
                                                       'Broker Code', 'Broker Name', 'Cash Broker Flag', 'Transaction Type', 'Base Net Proceed Amount',
                                                       'Base Interest',	'Shares/Par Value',	'Performed CA',	'Month To Date ROR', 'Beginning Mkt Value',
                                                       '1 Day Value Added',	'Average Balance',	'Ending Market Value',	'Net Cash Flow'])

print(partOfMergedSortedData.head())
'''