import streamlit as st
import pandas as pd
import mysql.connector
from app1 import *

# Load the logo image
st.set_page_config(page_title="GEMSQL", page_icon=":bookmark_tabs:")

# CSS for styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cambria&display=swap');
    
    body {
        font-family: 'Cambria', serif;
    }
    .header {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 20px;
    }
    .logo {
        margin-right: 20px;
    }
    .title {
        text-align: center;
        border-bottom: 2px solid #000; /* Underline */
        padding-bottom: 5px; /* Space between text and underline */
    }
    .subtitle {
        text-align: center;
        border-bottom: 2px solid #000; /* Underline */
        padding-bottom: 5px; /* Space between text and underline */
        margin-bottom: 20px;
    }
    .submit-button {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .submit-button button {
        font-weight: bold;
    }
    .color-patch {
        background-color: #E0F7FA; /* Light pastel color */
        padding: 20px 0;
        margin-bottom: 20px;
    }
    .answer-title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
    }
    .answer-content {
    font-size: 20px;
    color: green; /* Green color for the answer */
    }
    .question {
        font-size: 20px; 
        font-weight: bold;
    }
    .stButton > button {
        display: block;
        margin: 0 auto;
        font-weight: bold;
        font-size: 18px;
    }
    .database-preview-title {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to get the first 2 rows of the database
def get_first_two_rows():
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            port = 3307,
            database="general_data"
        )
        
        # Query to select the first 2 rows from the general_data table
        query = "SELECT * FROM indiavotes LIMIT 2"
        
        # Execute the query and fetch the results into a pandas DataFrame
        df = pd.read_sql_query(query, conn)
        
        # Close the database connection
        conn.close()
        
        return df
    except Exception as e:
        st.error(f"An error occurred while fetching data: {str(e)}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

# Container for all elements
# Color patch
st.markdown("<div class='color-patch'>", unsafe_allow_html=True)

# Header with logo and title
st.markdown(
    f"""
    <div class='header'>
        <div class='title'>
            <h1><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24"><path fill="currentColor" d="M11.04 19.32Q12 21.51 12 24q0-2.49.93-4.68q.96-2.19 2.58-3.81t3.81-2.55Q21.51 12 24 12q-2.49 0-4.68-.93a12.3 12.3 0 0 1-3.81-2.58a12.3 12.3 0 0 1-2.58-3.81Q12 2.49 12 0q0 2.49-.96 4.68q-.93 2.19-2.55 3.81a12.3 12.3 0 0 1-3.81 2.58Q2.49 12 0 12q2.49 0 4.68.96q2.19.93 3.81 2.55t2.55 3.81"/></svg>     
            GEMSQL</h1>
            <h3>Text to SQL Converter</h3>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# End of color patch
st.markdown("</div>", unsafe_allow_html=True)

# Display the first 2 rows of the database
st.markdown("<p class='database-preview-title'>Database Preview (First 2 Rows):</p>", unsafe_allow_html=True)
df = get_first_two_rows()
if not df.empty:
    st.table(df)
else:
    st.warning("No data available to display.")

# Input field with increased font size
st.markdown("<p class='question'>Question:</p>", unsafe_allow_html=True)
question = st.text_input("", key="question_input")

# Submit button (centered by CSS)
submit = st.button("SUBMIT", key="submit_button")

if question and submit:
    chain = get_db_chain()
    result = execute_query(chain, question)
    answer = result.get("result")
    query = result.get("query")
    
    st.markdown("<p class='answer-title'>Answer:</p>", unsafe_allow_html=True)
    st.markdown(f"<div class='answer-content'> {answer}</div>", unsafe_allow_html=True)
    st.markdown(f"<br>", unsafe_allow_html=True)
    st.markdown(f"<div class='query-content'>Query: {query}</div>", unsafe_allow_html=True)


st.markdown("</div>", unsafe_allow_html=True)