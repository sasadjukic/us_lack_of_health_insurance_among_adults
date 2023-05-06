
'''
    help module to store function that will be called across the package many times
'''

import pandas as pd

def get_health_insurance_dataframe(data: pd.DataFrame) -> pd.DataFrame:
    '''get the right survey question'''
    h_insurance = data[data['question'] == 'Current lack of health insurance among adults aged 18-64 years']
    return h_insurance

def get_nationwide_only(data: pd.DataFrame) -> pd.DataFrame:
    '''get only US data'''
    nationwide = data.loc[(data['locationabbr']) == 'US']
    return nationwide

def get_us_states_only(data: pd.DataFrame) -> pd.DataFrame:
    '''get only 50 US states + DC'''
    states = data.loc[
                        (data['locationdesc'] != 'United States') &
                        (data['locationdesc'] != 'Puerto Rico') &
                        (data['locationdesc'] != 'Guam') &
                        (data['locationdesc'] != 'Virgin Islands')
                    ]

    return states

# this function is a visual helper to trim DataFrame to relevent columns, otherwise it's not necessary
def get_health_insurance_value_columns(main: pd.DataFrame) -> pd.DataFrame:
    '''get only relevant columns'''
    value_columns = main[['yearstart', 'locationabbr', 'datavaluealt',  'stratification1', 'datavaluetype']]
    return value_columns

def get_crude_prevelance(data: pd.DataFrame) -> pd.DataFrame:

    c_prev = data[
                  (data['stratification1'] == 'Overall') & 
                  (data['datavaluetype'] == 'Crude Prevalence')
                ]
    
    return c_prev

def get_2011_data(data: pd.DataFrame) -> pd.DataFrame:
    '''get data for 2011'''
    year_2011 = data[(data['yearstart'] == 2011)]

    return year_2011

def get_2012_data(data: pd.DataFrame) -> pd.DataFrame:
    '''get data for 2012'''
    year_2012 = data[(data['yearstart'] == 2012)]

    return year_2012

def get_2013_data(data: pd.DataFrame) -> pd.DataFrame:
    '''get data for 2013'''
    year_2013 = data[(data['yearstart'] == 2013)]

    return year_2013

def get_2014_data(data: pd.DataFrame) -> pd.DataFrame:
    '''get data for 2014'''
    year_2014 = data[(data['yearstart'] == 2014)]

    return year_2014

def get_2015_data(data: pd.DataFrame) -> pd.DataFrame:
    '''get data for 2015'''
    year_2015 = data[(data['yearstart'] == 2015)]

    return year_2015

def get_2016_data(data: pd.DataFrame) -> pd.DataFrame:
    '''get data for 2016'''
    year_2016 = data[(data['yearstart'] == 2016)]

    return year_2016

def get_2017_data(data: pd.DataFrame) -> pd.DataFrame:
    '''get data for 2017'''
    year_2017 = data[(data['yearstart'] == 2017)]

    return year_2017

def get_2018_data(data: pd.DataFrame) -> pd.DataFrame:
    '''get data for 2018'''
    year_2018 = data[(data['yearstart'] == 2018)]

    return year_2018

def get_2019_data(data: pd.DataFrame) -> pd.DataFrame:
    '''get data for 2019'''
    year_2019 = data[(data['yearstart'] == 2019)]

    '''
        New Jersey is missing data for this year
        I had assign average value for last five years to NJ
    '''
    year_2019.loc[925428, 'datavaluealt'] = 13.60

    return year_2019

def get_2020_data(data: pd.DataFrame) -> pd.DataFrame:
    '''get data for 2020'''
    year_2020 = data[(data['yearstart'] == 2020)]

    return year_2020

def get_2021_data(data: pd.DataFrame) -> pd.DataFrame:
    '''get data for 2021'''
    get_2021 = data[(data['yearstart'] == 2021)]

    '''
        Florida is missing data for this year
        I had assign average value for last five years to FL
    '''
    get_2021.loc[636591, 'datavaluealt'] = 21.20

    return get_2021