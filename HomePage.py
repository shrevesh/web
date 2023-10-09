import streamlit as st
import webbrowser

st.title("IITI SOC '23")

st.markdown (""" # Retail Store Sales Forecasting """ )

st.markdown( """We have taken the data set of a retail store chain which shows its weekly sales store and departmentwise. From that we have selected a single store with 5 departments to forecast the departmentwise sales. We preprocessed the data and tried implementing various time-series models and the chose the one which gave the best results. Along with the forcasting, we also created DashBoards for Visualization of the Data. \n
We have made two Dahsboard \n
Dashboard 1 shows the Charts and Visulaizations of the current data set. It contains charts suct as Line Chart, Pie Charts and other features such as Query Tables. \n
Dashboard 2 shows the Forecasted Sales using a line chart where you can selcet which department you want to see. \n
We have also added the link of the GitHub Repository which was used to deploy this and it also contains the Jupyter Notebook
            """
)

st.markdown ("""
###
## 1) Charts and Statistics of Current Data """)
# Create an st.button
if st.button("DashBoard 1",key='button1'):
    # Define the URL you want to open
    url_to_open = "https://retail-store-forecasting-dashboard1.streamlit.app/"  
    # Using a Webbrowser Function to open the URL when Button is clicked
    webbrowser.open_new_tab(url_to_open)
    
st.markdown (""" ## 2) Predicted Future Patterns and Measures""")
#Button 2
if st.button("DashBoard 2",key='button2'):
    # Define the URL you want to open
    url_to_open = "https://retail-store-forecasting-dashboard2.streamlit.app/"  
    # Using a Webbrowser Function to open the URL when Button is clicked
    webbrowser.open_new_tab(url_to_open)

st.markdown ("""
###
### GitHub Repository Link """)
#Button 2
if st.button("GitHub",key='button3'):
    # Define the URL you want to open
    url_to_open = "https://github.com/shrevesh/Retail-Store-Sales-Forcasting"  
    # Using a Webbrowser Function to open the URL when Button is clicked
    webbrowser.open_new_tab(url_to_open)

# Define a function to create a button with a hyperlink appearance
def hyperlink_button(label, link):
    button_html = f'<a href="{link}" target="_blank" class="stButton">{label}</a>'
    st.markdown(button_html, unsafe_allow_html=True)

# Usage
hyperlink_button("Click me to visit OpenAI", "https://github.com/shrevesh/Retail-Store-Sales-Forcasting")


st.markdown ("""
### Team Members\n 1) Gulshan Kumar \n 2) S Shrevesh
              
### Mentors \n 1) Devansh \n  2) Nilay Ganvit  
""")
                       
