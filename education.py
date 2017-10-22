from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas as pd

path = "/users/yuanhsinhuang/desktop/projects/visual/bokeh/input/bachelors.csv"

df = pd.read_csv(path)
x = df["Year"]
y = df["Engineering"]

output_file("education.html")

f = figure()
f.line(x,y)

show(f)
