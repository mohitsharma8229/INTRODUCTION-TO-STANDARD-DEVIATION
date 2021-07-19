import plotly.express as px
import csv
import numpy as np
def getDataSource(data_path):
    tem=[]
    ice_sales=[]
    with open (data_path)as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            tem.append(float(row["Temperature"]))
            ice_sales.append(float(row["Ice-cream Sales"]))
    return {"x":tem,"y":ice_sales}

def findCorrelation(datasourcs):
    Correlation=np.corrcoef(datasourcs["x"],datasourcs["y"])
    print ("Correlation",Correlation[0,1])

def setup():
    data_path="tem.csv"
    datasourcs=getDataSource(data_path)
    findCorrelation(datasourcs)

setup()