# -*- coding: utf-8 -*-
"""
Datatype infer Core
"""
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
        types = {}

        for col in self.columns:
            if self.pandas_types[col].kind == 'O':
                if self._verify_dateutil(col):
                    types[col] = 'DateTime'
                else:
                    types[col] = 'Categorical'
            else:
                types[col] = 'Numerical'

        self.types = types

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
