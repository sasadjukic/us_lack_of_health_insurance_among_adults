
# import libraries and modules
import pandas as pd 
from main_data import usa_data
from us_health_insurance_help import (
                                      get_health_insurance_dataframe, 
                                      get_us_states_only,
                                      get_crude_prevelance,
                                      get_2011_data,
                                      get_2012_data,
                                      get_2013_data,
                                      get_2014_data,
                                      get_2015_data,
                                      get_2016_data,
                                      get_2017_data,
                                      get_2018_data,
                                      get_2019_data,
                                      get_2020_data,
                                      get_2021_data
                                     )


# get data from imported modules
health_insurance = get_health_insurance_dataframe(usa_data)
states_only = get_us_states_only(health_insurance)
crude_prevelance = get_crude_prevelance(states_only)

def get_top_10_uninsured_states_2021(d_2021: pd.DataFrame):
    '''get top 10 uninsured states for 2021'''

    return d_2021.nlargest(10, columns='datavaluealt')

def get_2011_values_for_2021_top_ten(d_2011: pd.DataFrame, top_2021: pd.DataFrame):
    '''get 2011 values for top uninsured states from 2021 to use as comparison'''

    top_2021_states = top_2021['locationabbr'].tolist()
    values_2011 = {}

    for i in d_2011.index:
        state = d_2011.loc[i, 'locationabbr']
        value = d_2011.loc[i, 'datavaluealt']
        if state in top_2021_states:
            values_2011[state] = value

    return values_2011

# get data by year 
states_2011 = get_2011_data(crude_prevelance)
states_2012 = get_2012_data(crude_prevelance)
states_2013 = get_2013_data(crude_prevelance)
states_2014 = get_2014_data(crude_prevelance)
states_2015 = get_2015_data(crude_prevelance)
states_2016 = get_2016_data(crude_prevelance)
states_2017 = get_2017_data(crude_prevelance)
states_2018 = get_2018_data(crude_prevelance)
states_2019 = get_2019_data(crude_prevelance)
states_2020 = get_2020_data(crude_prevelance)
states_2021 = get_2021_data(crude_prevelance)
top_10_uninsured_states = get_top_10_uninsured_states_2021(states_2021)
values_2011_for_2021_top_ten = get_2011_values_for_2021_top_ten(states_2011, top_10_uninsured_states)


