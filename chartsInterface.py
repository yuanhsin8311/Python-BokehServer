from bokeh.charts import Scatter
from bokeh.io import output_file, show
import pandas

df=pandas.read_csv("data.csv")

p=Scatter(df,"x","y")

output_file("Line_from_charts.html")

show(p)


