from sp import df
from bokeh.plotting import figure, show, output_file

p =figure(x_range='datetime', height=100, width=500,reponsive=True, title="Motion Graph")
q =p.quad(left=df["Start"],right=df["End"],bottom=0,top=1,color="green")

output_file("Graph1.html")
show(p)