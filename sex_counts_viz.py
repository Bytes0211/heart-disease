import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, LabelSet

# Read the CSV file
df = pd.read_csv('heart-disease.csv')

# Count males and females
sex_counts = df['Sex'].value_counts()

# Prepare data for Bokeh
categories = ['Male', 'Female']
counts = [sex_counts['M'], sex_counts['F']]

source = ColumnDataSource(data=dict(categories=categories, counts=counts, colors=['#3498db', '#e74c3c']))

# Create the figure
p = figure(x_range=categories, 
           height=400, 
           width=600,
           title="Male vs Female Count in Heart Disease Dataset",
           toolbar_location=None,
           tools="")

# Add vertical bars
p.vbar(x='categories', 
       top='counts', 
       width=0.5, 
       source=source,
       color='colors',
       alpha=0.8)

# Add labels on top of bars
labels = LabelSet(x='categories', y='counts', text='counts', 
                  level='glyph', x_offset=-10, y_offset=5,
                  source=source, text_font_size='12pt', text_font_style='bold')
p.add_layout(labels)

# Styling
p.xgrid.grid_line_color = None
p.y_range.start = 0
p.xaxis.axis_label = "Sex"
p.yaxis.axis_label = "Count"
p.xaxis.axis_label_text_font_size = "12pt"
p.yaxis.axis_label_text_font_size = "12pt"
p.title.text_font_size = "14pt"

# Output to HTML file
output_file("sex_counts_visualization.html")

# Show the plot
show(p)
