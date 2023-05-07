
# import necessary paths and libraries to use in chartmaking
import os, sys
import pandas as pd 
import matplotlib.pyplot as plt

# add path to list of python paths to import modules
userprofile = os.getenv('USERPROFILE')
file_path = f'{userprofile}\Desktop\github\\us_lack_of_health_insurance_among_adults'
sys.path.append(file_path)

# import module with necessary data
from us_lack_of_health_insurance import lack_of_insurance_2011_2021

def display_line_chart_of_us_lack_of_health_insurance_2011_2021(data: pd.DataFrame) -> None:
    '''
        display line chart of precentage of people lacking health insurance in the US from 2011-2021
    '''
    # set our variables to display
    years = data['yearstart'].tolist()
    values = data['datavaluealt'].tolist()

    # set colors
    bg_color = '#0a4157'
    line_color = '#fdf7c3'
    text_color = '#c0621d'
    subdued_text = '#dca781'

    # make plots
    fig, ax = plt.subplots()
    plt.plot(years, values, marker='o', color=line_color, linestyle='solid')

    # change plots bg and box colors
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    # modify box edges
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color(subdued_text)
    ax.spines['left'].set_color(subdued_text)

    # modify x and y ticks
    plt.xticks([x for x in range(2011, 2022)], color = subdued_text)
    plt.yticks(color = subdued_text)

    # reverse values in a list to display them in the chart
    values.reverse()
    for index, value in enumerate(values):
        plt.text(
            index, 
            value, 
            f'{str(value)}%',
            position = (index +2011, value+0.35),
            color = text_color,
            fontweight = 'bold',
            fontsize = 15
        )

    plt.show() 

print(display_line_chart_of_us_lack_of_health_insurance_2011_2021(lack_of_insurance_2011_2021))



