import pandas as pd
import plotly.express as px
df=pd.read_csv("data.csv")
fig=px.scatter(df,x="Population",y="Per capita",size="Percentage",color="Country",size_max=60)
##fig=px.bar(df,x="Country",y="InternetUsers")
##df=pd.read_csv("line.csv")
##fig=px.line(df,x="Year",y="Per capita income",color="Country",title="percapita income")
fig.show()