'''
Script to make an interactivate Bokeh plot to show how each
person graded the different wines in this test.

Require python packages: pandas, bokeh

To run:

    bokeh serve --show individual_scores.py

'''
import pandas as pd

from bokeh.io import curdoc
from bokeh.layouts import row
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure


def get_dataset(src, name):
    df = src[name].copy()
    data = {'price':df.index.to_list(),
            'rating':df.to_list()}

    return ColumnDataSource(data)

def make_plot(source1,source2, title):
    plot = figure(plot_width=800, tools="", toolbar_location=None,
                  y_range=(-0.5,5.5))
    plot.title.text = title
    plot.title.text_font_size = '18pt'

    plot.line(source=source1,x='price',y='rating',
              color='maroon', line_width=3, legend_label='Red wine')
    plot.circle(source=source1,x='price',y='rating',
                color='maroon', size=10, legend_label='Red wine')

    plot.line(source=source2,x='price',y='rating',
              color='goldenrod', line_width=3, legend_label='White wine')
    plot.circle(source=source2,x='price',y='rating',
                color='goldenrod', size=10, legend_label='White wine')

    # fixed attributes
    plot.xaxis.axis_label = 'Price [$]'
    plot.xaxis.axis_label_text_font_size = '14pt'

    plot.yaxis.axis_label = 'Rating'
    plot.yaxis.axis_label_text_font_size = '14pt'

    plot.xaxis.major_label_text_font_size = '12pt'
    plot.yaxis.major_label_text_font_size = '12pt'

    return plot

def update_plot(attrname, old, new):
    name = name_select.value
    plot.title.text = name

    src = get_dataset(df_red,name)
    source_red.data.update(src.data)

    src = get_dataset(df_wht,name)
    source_wht.data.update(src.data)



df_red = pd.read_csv('../data/SS3_red.csv',index_col='price')
del df_red['Name']
del df_red['Averages']
df_red.sort_index(inplace=True)

df_wht = pd.read_csv('../data/SS3_white.csv',index_col='price')
del df_wht['Name']
del df_wht['Averages']
df_wht.sort_index(inplace=True)


name_select = Select(value='Roberto',title='Pick a sommelier', 
                     options=df_red.columns.to_list())

source_red = get_dataset(df_red,'Roberto')
source_wht = get_dataset(df_wht,'Roberto')
plot = make_plot(source_red,source_wht, 'Roberto')

name_select.on_change('value', update_plot)

curdoc().add_root(row(plot, name_select))
curdoc().title = "Science Saturday 3"

