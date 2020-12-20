from bokeh.plotting import figure,output_file,show
from bokeh.models import ColumnDataSource,Select
from bokeh.layouts import row
from bokeh.io import curdoc,show,output_file
import pandas as pd

#Reading in the data and cleaning up a little
red = pd.read_csv('../data/SS3_red.csv',index_col='price')
del red['Name']
del red['Averages']
red.sort_index(inplace=True)

wht = pd.read_csv('../data/SS3_white.csv',index_col='price')
del wht['Name']
del wht['Averages']
wht.sort_index(inplace=True)

red_src = ColumnDataSource(data=red)
wht_src = ColumnDataSource(data=wht)

def update_plot(attr, old, new):
    # If the new Selection is 'female_literacy', update 'y' to female_literacy
    if new == 'female_literacy':
        source.data = {
            'x' : fertility,
            'y' : female_literacy
        }
    # Else, update 'y' to population
    else:
        source.data = {
            'x' : fertility,
            'y' : population
        }


select = Select(title = "Select drinker:", 
                value = "", 
                options = [""] + red.columns.to_list()
                )

# Create a new plot: plot
p = figure(y_range=(-0.5,5.5))

# Add circles to the plot
p.line('price', 'Roberto',source=red_src,color='maroon',
        line_width=3,
        legend_label='Red wine')
p.circle('price', 'Roberto',source=red_src,color='maroon',
        legend_label='Red wine',
        size=10)

p.line('price', 'Roberto',source=wht_src,color='goldenrod',
        line_width=3,
        legend_label='White wine')
p.circle('price', 'Roberto',source=wht_src,color='goldenrod',
        legend_label='White wine',
        size=10)

p.xaxis.axis_label = 'Price [$]'
p.xaxis.axis_label_text_font_size = '14pt'
#p.xaxis.axis_label_text_font_style = 'bold'

p.yaxis.axis_label = 'Rating'
p.yaxis.axis_label_text_font_size = '14pt'
#p.yaxis.axis_label_text_font_style = 'bold'

p.xaxis.major_label_text_font_size = '12pt'
p.yaxis.major_label_text_font_size = '12pt'


# Create a dropdown Select widget: select
#select = Select(title="distribution", options=['female_literacy', 'population'], value='female_literacy')

# Attach the update_plot callback to the 'value' property of select
select.on_change('value', update_plot)

# Create layout and add to current document
layout = row(select,p)
curdoc().add_root(layout)


#output_file('test.html')
show(p)
