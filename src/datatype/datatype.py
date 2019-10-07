# -*- coding: utf-8 -*-
"""
Datatype infer Core
"""
import json
from dateutil.parser import parse
import pandas as pd


class DataFrame:
    '''
    Simple pandas dataframe wrapper.
    '''

    def __init__(self, dataframe):
        self._types = {}

        # Slice DataSet for better performance
        self._dataframe = dataframe[:2000]

        self._pandas_types = dataframe.dtypes
        self._columns = dataframe.columns.values

    @property
    def types(self):
        '''
        DataFrame columns datatypes.
        '''
        return self._types

    @types.setter
    def types(self, types):
        self._types = types

    @property
    def dataframe(self):
        '''
        DataFrame body.
        '''
        return self._dataframe

    @property
    def pandas_types(self):
        '''
        Pandas infered columns dtypes.
        '''
        return self._pandas_types

    @property
    def columns(self):
        '''
        DataFrame columns names.
        '''
        columns = []
        for col in self._columns:
            columns.append({'name': col})

        return json.dumps(columns)

    @staticmethod
    def get_dataframe_from_csv(path):
        '''
        Static method to get DataFrame from csv path.
        '''
        dataframe = pd.read_csv(path, sep=None, engine='python')
        return DataFrame(dataframe)

    def infer_types(self):
        '''
        Method to infer data type from DataSet columns.
        This method iterates over columns and pick the
        types inferred by pandas.
        For Object types, checks if it is DateTime or
        Categorical.
        '''
        columns = []

        for col in self.columns:
            if self.pandas_types[col].kind == 'O':
                if self._verify_dateutil(col):
                    columns.append({'name': col, 'datatype': 'DateTime'})
                else:
                    columns.append(
                        {'name': col, 'datatype': 'Categorical'})
            else:
                columns.append({'name': col, 'datatype': 'Numerical'})

        self.types = json.dumps({"columns": columns})

    def _verify_dateutil(self, column_name):
        '''
        Method to verify if a column is of DateTime type.
        '''
        column = self.dataframe[column_name]

        for _, value in column.iteritems():
            try:
                parse(value)
                break
            except ValueError:
                return False
        return True


class Header:
    '''
    Simple pandas header wrapper.
    '''

    def __init__(self, header):
        self._header = header

    @property
    def header(self):
        '''
        Header body.
        '''
        datatypes = []
        for line in self._header:
            datatypes.append({'datatype': line})

        return json.dumps(datatypes)

    @staticmethod
    def get_header_from_txt(path):
        '''
        Static method to get header from txt path.
        '''
        with open(path, 'r') as f:
            lines = f.read().splitlines()

        return Header(lines)


if __name__ == '__main__':
    HEADER = Header.get_header_from_txt('./src/datatype/tests/data/header.txt')

    print(HEADER.header)

    DATAFRAME = DataFrame.get_dataframe_from_csv(
        './src/datatype/tests/data/data.csv')

    print(DATAFRAME.columns)
