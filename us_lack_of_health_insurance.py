
'''
    import necessary modules and libraries
'''
import pandas as pd 
from main_data import usa_data
from us_health_insurance_help import (
                                        get_health_insurance_dataframe,
                                        get_nationwide_only,
                                    )

def get_crude_prevelance(data: pd.DataFrame) -> pd.DataFrame:
    '''get data for for overall population and crude prevelance'''
    c_prev = data[
                  (data['stratification1'] == 'Overall') & 
                  (data['datavaluetype'] == 'Crude Prevalence') 
                ]

    return c_prev

def sort_crude_prev_data_by_years(data: pd.DataFrame) -> pd.DataFrame:
    '''sort years in descending form'''
    return data.nlargest(11, columns='yearstart')

def get_values_by_year(data: pd.DataFrame) -> pd.DataFrame:
    '''get data frame with only two necessary columns (survey years, percentage of uninsured population)'''
    return data[['yearstart', 'datavaluealt']]

health_insurance = get_health_insurance_dataframe(usa_data)
nationwide = get_nationwide_only(health_insurance)
crude_prevelance = get_crude_prevelance(nationwide)
lack_of_insurance_by_year = sort_crude_prev_data_by_years(crude_prevelance)
lack_of_insurance_2011_2021 = get_values_by_year(lack_of_insurance_by_year)


