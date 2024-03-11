# Import python packages
import streamlit as st
import pandas as pd
import pandasai
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
import snowflake.connector
import pygwalker as pyg
import streamlit.components.v1 as components

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)
 

# Establish connection to Snowflake
conn = snowflake.connector.connect(
    user='',
    password='',
    account='',
    warehouse='',
    database='',
    schema=''
)

# Run a query and save the data as a DataFrame
query = """select 
                * 
                from 
                some_table_name
            """
df = pd.read_sql_query(query, conn)

# Generate the HTML using Pygwalker
pyg_html = pyg.to_html(df)

# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)
