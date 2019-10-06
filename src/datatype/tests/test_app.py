# -*- coding: utf-8 -*-
'''
Tests of App Core
'''

from datatype.datatype import DataFrame


def test_dataframe():
    '''
    DataFrame class unit test
    '''

    dataframe = DataFrame.get_dataframe_from_csv(
        'src/datatype/tests/data/data.csv')

    dataframe.infer_types()

    print(dataframe.types)

    assert dataframe.types == {'columns':
                               [{'name': 'Transaction_date', 'datatype': 'DateTime'},
                                {'name': 'Product', 'datatype': 'Categorical'},
                                {'name': 'Price', 'datatype': 'Numerical'},
                                {'name': 'Payment_Type', 'datatype': 'Categorical'},
                                {'name': 'Name', 'datatype': 'Categorical'},
                                {'name': 'City', 'datatype': 'Categorical'},
                                {'name': 'State', 'datatype': 'Categorical'},
                                {'name': 'Country', 'datatype': 'Categorical'},
                                {'name': 'Account_Created',
                                    'datatype': 'DateTime'},
                                {'name': 'Last_Login', 'datatype': 'DateTime'},
                                {'name': 'Latitude', 'datatype': 'Numerical'},
                                {'name': 'Longitude', 'datatype': 'Numerical'}
                                ]
                               }


test_dataframe()
