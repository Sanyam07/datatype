# -*- coding: utf-8 -*-
'''
Tests of App Core
'''
import json
from datatype.datatype import DataFrame


def test_dataframe():
    '''
    DataFrame class unit test
    '''

    dataframe = DataFrame.get_dataframe_from_csv(
        'src/datatype/tests/data/data.csv')

    dataframe.infer_types()

    print(dataframe.types)

    assert dataframe.types == json.dumps({'columns':
                                          [{'name': 'Transaction_date', 'datatype': 'DateTime'},
                                           {'name': 'Product',
                                              'datatype': 'factor'},
                                           {'name': 'Price',
                                            'datatype': 'numeric'},
                                           {'name': 'Payment_Type',
                                            'datatype': 'factor'},
                                           {'name': 'Name',
                                            'datatype': 'factor'},
                                           {'name': 'City',
                                            'datatype': 'factor'},
                                           {'name': 'State',
                                            'datatype': 'factor'},
                                           {'name': 'Country',
                                            'datatype': 'factor'},
                                           {'name': 'Account_Created',
                                              'datatype': 'DateTime'},
                                           {'name': 'Last_Login',
                                            'datatype': 'DateTime'},
                                           {'name': 'Latitude',
                                            'datatype': 'numeric'},
                                           {'name': 'Longitude',
                                            'datatype': 'numeric'}
                                           ]
                                          })


test_dataframe()
