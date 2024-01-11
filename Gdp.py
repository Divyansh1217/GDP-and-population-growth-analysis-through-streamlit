import pandas as pd
import plotly.express as px
import numpy as np
import streamlit as st
data=pd.read_csv("indianEco.csv")
fig=px.line(data,x="Year",y=data.columns[9:11])
gdp=px.line(data,x="Year",y=data.columns[2:8])
st.header("INDIA")
st.plotly_chart(fig)
st.plotly_chart(gdp)
st.dataframe(data)