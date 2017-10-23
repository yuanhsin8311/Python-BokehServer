#Making a basic Bokeh line graph

#importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show, save

#prepare some data
x=[1,2,3,4,5]
y=[6,7,8,9,10]

#prepare the output file
output_file("Line_from_plotting.html")

#create a figure object
f=figure()

#create circle plot
f.circle(x,y)

#write the plot in the figure object
show(f)


