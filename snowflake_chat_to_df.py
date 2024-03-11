# Import python packages
import streamlit as st
import pandas as pd
import pandasai
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
import snowflake.connector

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

# Create a SmartDataframe object
llm = OpenAI(api_token="use_openai_api_key")
smart_df = SmartDataframe(df, config={"llm": llm})

# Display the DataFrame
st.dataframe(df)

# Create a text box for user input
user_question = st.text_input("Ask a question about the data:")

# If the user has entered a question, get the answer and display it
if user_question:
    answer = smart_df.chat(user_question)
    st.write(answer)
