
import matplotlib.pyplot as plt 

def display_top_ten_states_comparison_2011_2021() -> None:

    '''
        dictionary is for display purpose only 
        all data in this dictionary is from us_states_lack_of_health_insurance_by_year.py
    '''

    states = {
        'AZ' : [22.4, 12.7],
        'AL' : [22.1, 12.9],
        'NC' : [24.8, 13.3],
        'GA' : [28.8, 16.8],
        'MS' : [30.7, 13.4],
        'NV' : [31.9, 13.9],
        'WY' : [24.7, 16.7],
        'OK' : [26.6, 14.3],
        'SC' : [25.3, 13.7],
        'TX' : [34.4, 23.9],
        
        
        
    }

    # put state values in a list
    values = [
              22.4, 12.7, 22.1, 12.9, 24.8, 13.3,
              28.8, 16.8, 30.7, 13.4, 31.9, 13.9,
              24.7, 16.7, 26.6, 14.3, 25.3, 13.7,
              34.4, 23.9
             ]

    # put assignment numbers to stems
    stems = [
                1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 
                6, 6, 7, 7, 8, 8, 9, 9, 10, 10
            ]

    # define all colors to use
    bg_color = '#b9e9fc'
    text_subdued = '#dca781'
    color_2021 = '#c0621d'

    #create stem chart base
    fig, ax = plt.subplots()
    marker, line, base = ax.stem(stems, values, basefmt=' ', orientation='horizontal')

    #modify chart base
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    # remove chart borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # modify look of stems
    plt.setp(line, linewidth=5, color=color_2021)
    plt.setp(marker, markersize=20, color=color_2021)

    # set x and y tick colors
    plt.xticks(color = text_subdued)
    plt.yticks(color = text_subdued)

    # set x and y limits
    plt.xlim([10, 36])
    plt.ylim([0, 11])

    plt.show()

display_top_ten_states_comparison_2011_2021()