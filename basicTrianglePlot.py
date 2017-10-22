from bokeh.plotting import figure
from bokeh.io import output_file, show

output_file("triangle.html")

x = [1,2,3,4,5]
y= [6,7,8,9,10]

f = figure()

f.triangle(x,y)

show(f)