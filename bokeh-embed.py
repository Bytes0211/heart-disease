from bokeh.plotting import figure, show, output_file, curdoc


output_file("line.html")
curdoc().theme = 'dark_minimal'

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
# create a new plot with a title and axis labels
p = figure(title="Steve's First Plot", x_axis_label="x", y_axis_label="y")

# add a line renderer with legend and line thickness
p.line(x, y, legend_label="Temp.", line_width=2)

p.xaxis.major_tick_line_color = None
p.yaxis.major_tick_line_color = None
p.xaxis.major_label_text_font_size = '0pt'
p.yaxis.major_label_text_font_size = '0pt'

# show the results
show(p)
