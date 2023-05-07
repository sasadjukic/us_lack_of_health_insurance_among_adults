
# import necessary paths and libraries to use in chartmaking
import os, sys
import pandas as pd 
import plotly.express as px 

# add path to list of python paths to import modules
userprofile = os.getenv('USERPROFILE')
file_path = f'{userprofile}\Desktop\github\\us_lack_of_health_insurance_among_adults'
sys.path.append(file_path)

# import data
from us_states_lack_of_health_insurance_by_year import states_2021 

def display_unisured_map(states: pd.DataFrame) -> None:
    '''display USA map with states colored to match their percentages of lack of insurance'''
    fig = px.choropleth(
                        states, 
                        locations='locationabbr',
                        locationmode='USA-states',
                        scope='usa',
                        color='datavaluealt',
                        range_color=[0,30],
                        color_continuous_scale=['#fdf7c3', '#c0621d']
          ).update_layout(
                        template='none',
                        plot_bgcolor='#b9e9fc',
                        paper_bgcolor = '#b9e9fc'
          )

    fig.show()

display_unisured_map(states_2021)




