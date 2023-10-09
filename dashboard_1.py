import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import base64
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
from io import BytesIO

st.title ("Dashboard 1")

#Importing the data into a Pandas Dataframe
raw_csv_data= pd.read_csv("md3.csv")

#Preprocessing the Data
df_comp = raw_csv_data.copy()

#Deleting the Unnecessary Columns
del df_comp['Store']
del df_comp['IsHoliday']
del df_comp['Dept']

#Converting the Long Data into A Tabular Format which is easy to work with
data1 = df_comp[:143]
data2 = df_comp[143:286]
data3 = df_comp[286:429]
data4 = df_comp[429:572]
data5 = df_comp[572:715]

d1 = []
d1[0:143] = data1.Weekly_Sales

d2 = []
d2[0:143] = data2.Weekly_Sales

d3 = []
d3[0:143] = data3.Weekly_Sales

d4 = []
d4[0:143] = data4.Weekly_Sales

d5 = []
d5[0:143] = data5.Weekly_Sales

data = data1.copy()
data['dept1'] = d1
data['dept2'] = d2
data['dept3'] = d3
data['dept4'] = d4
data['dept5'] = d5


del data['Weekly_Sales']

#Renaming the Columns to make it Easier for Plotting Functions
data.columns = ["Date","Department 1", "Department 2", "Department 3", "Department 4", "Department 5"]

#Converting Str to datetime format
for index in data.index:
    x=data.loc[index,'Date']
    d = pd.to_datetime(x)
    f=d.date()
    data.loc[index,'Date'] = f

data1 = data.copy()

#Sidebar Code
st.sidebar.subheader("Navigation Bar")
rad = st.sidebar.radio("Select One of the following Options", {'Line Chart', 'Yearwise Avg Weekly Sales Data', 'Total Sales Data', 'Queries Table' , 'Pie Chart' })

#Linechart Selectbox
if rad == 'Line Chart':
    st.subheader ('LineChart to show the Sales for the Selected Department')
    yval= st.selectbox("Enter the Department",["Department 1", "Department 2", "Department 3", "Department 4", "Department 5","All"],index=0)

    if yval == 'All':
        yval = None

    #Linechart plot
    st.line_chart(data1, x='Date', y=yval)




#Yearwise Avg Weekly Sales Table
if rad == 'Yearwise Avg Weekly Sales Data':
    st.subheader ('Bar Chart showing the Yearwise Average Weekly Sales of the Selected Department ')
    dataY = data1.copy()
    yrs= []
    for index in data1.index:
        x=data1.loc[index,'Date']
        y = x.year
        yrs.append(y)

    dataY['Year_W']= yrs

    avg = st.selectbox("Enter the Department to see its Yearwise Average Weekly Sales ", 
                       ["Department 1", "Department 2", "Department 3", "Department 4", "Department 5"], index=0)
    key_sales_column = avg

    avg_sales = dataY.groupby('Year_W')[key_sales_column].mean().round()
    avg_sales = avg_sales.reset_index()

    

    Year = avg_sales['Year_W']
    Average_Sales = avg_sales[key_sales_column]

    as2 = pd.DataFrame()
    as2['Year'] = avg_sales['Year_W']
    as2['Average Sales'] = avg_sales[key_sales_column]
    
    #Plotting Bar Graph
    st.bar_chart(as2, x='Year', y='Average Sales')

    #Diplaying Dataframe
    st.dataframe(as2)

#Total Sales Data
if rad == 'Total Sales Data':
    st.subheader ('Bar Chart showing the Total Sales of each Department ')
    data2 = data1.copy()
    del data1['Date']
    sun = data1.sum().reset_index()
    #The sum() function applied to a DataFrame returns a Series object, not another DataFrame, 
    # so you cannot assign column names to it directly.

    sun.columns = ['Department','Total Sales']
    #Plotting Bar Graph
    st.bar_chart(sun, x='Department', y='Total Sales')


#Pie Chart
if rad == 'Pie Chart':
    st.subheader ('Pie Chart showing the contribution of each Department for selected Year and Month')
    df = data1.copy()

    df['Date'] = pd.to_datetime(df['Date'])
    
    unique_years = df['Date'].dt.year.unique()
    unique_months = ['January', 'February', 'March', 'April', 'May', 'June',
                        'July', 'August', 'September', 'October', 'November', 'December']
                       
    print(unique_months)

    # Create Streamlit widgets for year and month selection
    selected_year = st.selectbox('Select Year:', unique_years)
    if selected_year == 2010:
        selected_month = st.selectbox('Select Month:', unique_months[1:])

    if selected_year == 2011:
        selected_month = st.selectbox('Select Month:', unique_months)

    if selected_year == 2012:
        selected_month = st.selectbox('Select Month:', unique_months[:10])

    #if statements are used because all years don not have all the months, it may show error

    #Creating a filtered DataFrame based on the Year and Months Selected by the User
    filtered_df = df[(df['Date'].dt.year == selected_year) & (df['Date'].dt.strftime('%B') == selected_month)]

    # Select only the department columns for analysis
    department_columns = ['Department 1', 'Department 2', 'Department 3', 'Department 4', 'Department 5']
    department_sales = filtered_df[department_columns].sum()

    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(department_sales, labels=department_sales.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

    # Display the pie chart in Streamlit
    st.pyplot(fig)

    # Optional: Display a table with department-wise sales for the selected period
    st.write("Department-wise Sales For Selected Year and Month")
    department_sales = department_sales.reset_index()
    department_sales = pd.DataFrame (department_sales)
    department_sales = department_sales.rename_axis(None, axis=1)
    st.dataframe(department_sales)
    #In this updated script:


#Query Table
if rad == 'Queries Table':
    st.subheader ('Run your Queries here')
    st.write("Set the Ranges to get the Filtered Data")

    #Date Range
    da1= st.date_input("Enter Start Date in YYYY/MM/DD format",value = datetime.date(2010, 2, 5),min_value = datetime.date(2010, 2, 5), max_value = datetime.date(2012, 10, 26))
    da2= st.date_input("Enter End Datein YYYY/MM/DD format", value = datetime.date(2012, 10, 26),min_value = datetime.date(2010, 2, 5), max_value = datetime.date(2012, 10, 26))

    sam = data1[data1['Date'] >= da1 ]
    sam1 = sam[sam['Date'] <= da2 ]

    #Value Range

    st.write("Choose the Departments for which you want to set a range")

    p1v=[14537,57593]
    p2v=[35819,65616]
    p3v=[6165,51160]
    p4v=[32497,47894]
    p5v=[11570,85677]

    cb1 = st.checkbox("Department 1",value=False)
    if cb1:
        p1v = st.slider("Department 1", value=[14537,57593], min_value=14537, max_value=57593, key='slider1keys')

    cb2 = st.checkbox("Department 2",value=False)
    if cb2:
        p2v = st.slider("Department 2", value=[35819,65616], min_value=35819, max_value=65616, key='slider1keys2')

    cb3 = st.checkbox("Department 3",value=False)
    if cb3:
        p3v = st.slider("Department 3", value=[6165,51160], min_value=6165, max_value=51160, key='slider3keys')

    cb4 = st.checkbox("Department 4",value=False)
    if cb4:
        p4v = st.slider("Department 4", value=[32497,47894], min_value=32497, max_value=47894, key='slider4keys')

    cb5 = st.checkbox("Department 5",value=False)
    if cb5:
        p5v = st.slider("Department 5", value= [11570,85677] , min_value=11570, max_value=85677, key='slider5keys')

    d1 = sam1[sam1['Department 1'] >= p1v[0] ]
    d11= d1[d1['Department 1'] <= p1v[1] ]

    d2 = d11[d11['Department 2'] >= p2v[0] ]
    d22= d2[d2['Department 2'] <= p2v[1] ]

    d3 = d22[d22['Department 3'] >= p3v[0] ]
    d33= d3[d3['Department 3'] <= p3v[1] ]

    d4 = d33[d33['Department 4'] >= p4v[0] ]
    d44= d4[d4['Department 4'] <= p4v[1] ]

    d5 = d44[d44['Department 5'] >= p5v[0] ]
    d55= d5[d5['Department 5'] <= p5v[1] ]

    #Tables to display
    cdisp = st.multiselect("Select the Columns to Display", ["Date","Department 1", "Department 2", "Department 3", "Department 4", "Department 5"])
    cdisp.sort()

    st.dataframe(d55[cdisp])

    df = d55[cdisp]

#To download the result of Quesries table
    st.subheader("Click the Download Button to Download the Filtered Data as a CSV file")
    if st.button('Download'):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # Convert DataFrame to base64
        href = f'<a href="data:file/csv;base64,{b64}" download="edited_data.csv">Download Edited CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)

    

