# -*- coding: utf-8 -*-
'''
Tests of App Core
'''

from datatype.app import DataFrame


def test_dataframe():
    '''
    DataFrame class unit test
    '''

    dataframe = DataFrame.get_dataframe_from_csv(
        'src/app/tests/data/data.csv')

    dataframe.infer_types()

    assert dataframe.types == {'Account_Created': 'DateTime',
                               'City': 'Categorical',
                               'Country': 'Categorical',
                               'Last_Login': 'DateTime',
                               'Latitude': 'Numerical',
                               'Longitude': 'Numerical',
                               'Name': 'Categorical',
                               'Payment_Type': 'Categorical',
                               'Price': 'Numerical',
                               'Product': 'Categorical',
                               'State': 'Categorical',
                               'Transaction_date': 'DateTime'}


test_dataframe()
