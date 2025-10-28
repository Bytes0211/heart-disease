import pandas as pd
from bokeh.plotting import figure, output_file, curdoc, show
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.transform import linear_cmap
from bokeh.palettes import RdYlGn11

curdoc().theme = 'dark_minimal'

# Load the data
df = pd.read_csv('heart-disease.csv')

# Calculate missing data percentage for each column
missing_data = df.isnull().sum()
missing_percentage = (missing_data / len(df)) * 100

# Create data for visualization
columns = list(df.columns)
missing_counts = missing_data.tolist()
missing_pcts = missing_percentage.tolist()
total_rows = [len(df)] * len(columns)

# Create ColumnDataSource
source = ColumnDataSource(data=dict(
    columns=columns,
    missing_counts=missing_counts,
    missing_pcts=missing_pcts,
    total_rows=total_rows
))

# Create figure
p = figure(
    x_range=columns,
    height=400,
    width=1000,
    title="Missing Data Analysis - Heart Disease Dataset",
    toolbar_location="above",
    tools="pan,wheel_zoom,box_zoom,reset,save"
)

# Create color mapper (reversed so green = less missing, red = more missing)
mapper = linear_cmap(
    field_name='missing_pcts',
    palette=RdYlGn11[::-1],
    low=0,
    high=max(missing_pcts) if max(missing_pcts) > 0 else 100
)

# Create bars
p.vbar(
    x='columns',
    top='missing_pcts',
    width=0.8,
    source=source,
    line_color="white",
    fill_color=mapper
)

# Add hover tool
hover = HoverTool(tooltips=[
    ("Column", "@columns"),
    ("Missing Count", "@missing_counts"),
    ("Missing %", "@missing_pcts{0.2f}%"),
    ("Total Rows", "@total_rows")
])
p.add_tools(hover)

# Styling
p.xaxis.axis_label = "Columns"
p.yaxis.axis_label = "Missing Data (%)"
p.xaxis.major_label_orientation = 45
p.xgrid.grid_line_color = None

# Output to HTML file
output_file("heat-map.html")
show(p)

print(f"Total rows in dataset: {len(df)}")
print("\nMissing data summary:")
for col, count, pct in zip(columns, missing_counts, missing_pcts):
    print(f"{col:20s}: {count:5d} missing ({pct:6.2f}%)")
