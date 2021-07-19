import csv
import plotly.express as px

with open("tem.csv")as f:
    df =csv.DictReader(f)
    fig=px.scatter(df,x="Temperature",y="Ice-cream Sales")
    fig.show()