import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import base64

st.title ("Dashboard 2 (Forecasted Sales)")

#Reading data from the CSV file saved from Jupyter Notebook
raw_csv_data= pd.read_csv("predictions1.csv")
data = raw_csv_data.copy()

#Renaming the Columns
data.columns = ["Date", 'dept1', 'dept2', 'dept3', 'dept4', 'dept5',
                     'Department 1', 'Department 2', 'Department 3', 'Department 4', 'Department 5']

#Converting Str to datetime format
for index in data.index:
    x=data.loc[index,'Date']
    d = pd.to_datetime(x)
    f=d.date()
    data.loc[index,'Date'] = f

data1 = data.copy()

#DropDown Menu asking the user to select department
yval= st.selectbox("Enter the Department to see current Weekly Sales and Forecasted Weekly Sales"
                   ,["Department 1", "Department 2", "Department 3", "Department 4", "Department 5"],index=0)

#Manipulating Strings
yn = str('dept') + str(yval[11])

#Creating New Dataframe to get correct label names - - limitations of st.line function
nd = pd.DataFrame()
nd['Date'] = data1[['Date']]
nd['Current Sales'] = data1[yn]
nd['Forecasted Sales'] =data1[yval]

# Display the chart in Streamlit
st.line_chart(nd, x='Date', y= None)












    

