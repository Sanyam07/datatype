# -*- coding: utf-8 -*-
"""
Datatype infer Core
"""
import chardet
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
        return self._columns

    @staticmethod
    def get_dataframe_from_csv(path):
        '''
        Static method to get DataFrame from csv path.
        '''
        with open(path, 'rb') as f:
            encoding = chardet.detect(f.readline())['encoding']

        dataframe = pd.read_csv(
            path, sep=None, engine='python', encoding=encoding)
        return DataFrame(dataframe)

    def infer_types(self):
        '''
        Method to infer data type from DataSet columns.
        This method iterates over columns and pick the
        types inferred by pandas.
        For Object types, checks if it is DateTime or
        factor.
        '''
        columns = []

        for col in self.columns:
            if self.pandas_types[col].kind == 'O':
                if self._verify_dateutil(col):
                    columns.append({'name': col, 'datatype': 'DateTime'})
                else:
                    columns.append(
                        {'name': col, 'datatype': 'factor'})
            else:
                columns.append({'name': col, 'datatype': 'numeric'})

        self.types = json.dumps({"columns": columns})

    def get_columns(self):
        columns = []
        for col in self.columns:
            columns.append({'name': col})

        return json.dumps(columns)

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

    def __init__(self, lines):
        self._lines = lines

    @property
    def lines(self):
        '''
        Header body.
        '''
        return self._lines

    @staticmethod
    def get_header_from_txt(path):
        '''
        Static method to get header from txt path.
        '''
        with open(path, 'r') as f:
            lines = f.read().splitlines()

        return Header(lines)

    def get_lines_json(self):
        result = []
        for line in self.lines:
            result.append({'datatype': line})

        return json.dumps(result)

    def update_line(self, position, new_datatype):
        lines = self.lines
        lines[int(position)] = new_datatype

        return lines


if __name__ == '__main__':
    # HEADER = Header.get_header_from_txt('./src/datatype/tests/data/header.txt')

    # # print(HEADER.get_lines_json())

    # # print(HEADER.update_line(1, 'DateTime'))

    DATAFRAME = DataFrame.get_dataframe_from_csv(
        './src/datatype/tests/data/data.csv')

    print(DATAFRAME.columns)
