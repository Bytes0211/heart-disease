from bokeh.plotting import figure, show, curdoc
from bokeh.layouts import gridplot
from bokeh.models import Label
import pandas as pd

curdoc().theme = 'dark_minimal'

df = pd.read_csv("heart-disease.csv")

categorical_cols = ["Sex", "ChestPainType", "FastingBS", "RestingECG", "ExerciseAngina", "ST_Slope", "HeartDisease"]

plots = []

for col in categorical_cols:
    # Get value counts for the categorical column
    value_counts = df[col].value_counts().sort_index()
    categories = [str(x) for x in value_counts.index]
    counts = value_counts.values
    
    # Create figure
    p = figure(x_range=categories, title=col, width=600, height=400,
               toolbar_location=None, tools="")
    
    # Add bars
    p.vbar(x=categories, top=counts, width=0.5)
    
    # Add data labels to each bar
    for i, (cat, count) in enumerate(zip(categories, counts)):
        label = Label(x=i, y=count, text=str(count),
                     text_align='center', text_baseline='bottom',
                     text_color='white', text_font_size='12pt')
        p.add_layout(label)
    
    plots.append(p)

# Arrange in 4x2 grid
grid = gridplot(plots, ncols=2)
show(grid)
