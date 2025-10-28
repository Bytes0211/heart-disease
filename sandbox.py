import pandas as pd
from bokeh.plotting import figure, show, curdoc, output_notebook, output_file
from bokeh.palettes import Bright6
from bokeh.models import ColumnDataSource, LabelSet
from bokeh.layouts import row, column

cols = ["Sex", "ChestPainType", "FastingBS", "RestingECG", "ExerciseAngina", "ST_Slope", "HeartDisease"]

hdv = pd.read_csv("heart-disease.csv", usecols=cols)

genders = ["Male", "Female"]
sex_counts_vals = hdv["Sex"].value_counts()
sex_counts = (int(sex_counts_vals["M"]), int(sex_counts_vals["F"]))
sex_count_strs = [str(sc) for sc in sex_counts]

# print("Sex counts:\n", sex_counts_vals)
fastings = ["0", "1"]
fast_counts_vals = hdv["FastingBS"].value_counts().sort_index()
fast_counts = (int(fast_counts_vals[0]), int(fast_counts_vals[1]))

hrt_dis = ["0", "1"]
hrt_dis_vals = hdv["HeartDisease"].value_counts().sort_index()
hrt_dis_counts = (int(hrt_dis_vals[0]), int(hrt_dis_vals[1]))

chst_pain = ['ATA', 'NAP', 'ASY', 'TA']
chst_pain_vals = hdv["ChestPainType"].value_counts()
chst_pain_counts = [int(chst_pain_vals[cp]) for cp in chst_pain]

rest_ecg = ['Normal', 'ST', 'LVH']
rest_ecg_vals = hdv["RestingECG"].value_counts()
rest_ecg_counts = [int(rest_ecg_vals[re]) for re in rest_ecg]


source1 = ColumnDataSource(data=dict(genders = genders
                                    , sex_counts = sex_counts
                                    , sex_colors = Bright6[:2]
                                    , sex_count_strs = sex_count_strs))

source2 = ColumnDataSource(data=dict(fastings = fastings
                                    , fast_counts = fast_counts
                                    , fast_colors = Bright6[2:4]))

source3 = ColumnDataSource(data=dict(hrt_dis = hrt_dis
                                    , hrt_dis_counts = hrt_dis_counts
                                    , hrt_dis_colors = Bright6[4:]))

source4 = ColumnDataSource(data=dict(chst_pain = chst_pain
                                    , chst_pain_counts = chst_pain_counts
                                    , chst_pain_colors = Bright6[2:]))
source5 = ColumnDataSource(data=dict(rest_ecg = rest_ecg
                                    , rest_ecg_counts = rest_ecg_counts
                                    , rest_ecg_colors = Bright6[:3]))


curdoc().theme = 'dark_minimal'
output_notebook(hide_banner=True)
# output_file("sandbox.html", title="Sandbox")

plt1 = figure(title = "Patient Sex", x_range=genders, width=250, height=300, toolbar_location=None)

plt1.vbar(x='genders', top='sex_counts', width=0.9, color='sex_colors', legend_field='genders', source=source1)
plt1.xgrid.grid_line_color = None
plt1.y_range.start = 0
plt1.y_range.end = 900
plt2 = figure(title = "Fasting Blood Sugar", x_range=["0", "1"], width=250, height=300, toolbar_location=None)
plt2.vbar(x='fastings', top='fast_counts', width=0.9, color='fast_colors', source=source2)
plt2.xgrid.grid_line_color = None
plt2.y_range.start = 0
plt2.y_range.end = 900
plt3 = figure(title = "Heart Disease", x_range=["0", "1"], width=250, height=300, toolbar_location=None)
plt3.vbar(x='hrt_dis', top='hrt_dis_counts', width=0.9, color='hrt_dis_colors', source=source3)
plt3.xgrid.grid_line_color = None
plt3.y_range.start = 0
plt3.y_range.end = 900
plt4 = figure(title = "Chest Pain Type", x_range=chst_pain, width=250, height=300, toolbar_location=None)
plt4.vbar(x='chst_pain', top='chst_pain_counts', width=0.9, color='chst_pain_colors', source=source4)
plt4.xgrid.grid_line_color = None
plt4.y_range.start = 0
plt4.y_range.end = 900
plt5 = figure(title = "Resting ECG", x_range=rest_ecg, width=250, height=300, toolbar_location=None)
plt5.vbar(x='rest_ecg', top='rest_ecg_counts', width=0.9, color='rest_ecg_colors', source=source5)
plt5.xgrid.grid_line_color = None
plt4.y_range.start = 0
plt5.y_range.start = 0
plt5.y_range.end = 900

label1 = LabelSet(x='genders', y='sex_counts', text='sex_count_strs', text_color="gainsboro"
                  ,level='glyph', x_offset=0, y_offset=5, source=source1)
plt1.add_layout(label1)

plt1.min_border_left=75
plt1.min_border_bottom=100
plt1.min_border_top=30
plt2.min_border_left=75
plt2.min_border_bottom=100
plt2.min_border_top=30
plt3.min_border_left=75
plt3.min_border_bottom=100
plt3.min_border_top=30
plt4.min_border_left=75
plt4.min_border_top=30
plt5.min_border_left=75
plt5.min_border_top=30

plot = column(row(plt1, plt2, plt3), row(plt4, plt5))
show(plot)