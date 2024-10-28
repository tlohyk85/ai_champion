import os
import streamlit as st
import pandas as pd
import numpy as np
from my_script import get_completion
from my_script import get_completion_workpass
from utility import check_password

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My AI Champion Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()

# endregion <--------- Streamlit Page Configuration --------->

os.environ['OPENAPI_API_KEY'] = st.secrets['OPENAPI_API_KEY']

def about_us():
  st.title("About Us Now")
  st.write("This application aims to empower users with information regarding the Primary Care Plan (PCP) and Work Passes for foreign workers in Singapore. We leverage external data sources, user input, and advanced language processing to deliver accurate and helpful insights.")
  
  st.header("Objectives")
  st.write("- Assist users with inquiries related to the PCP and Work Passes for foreign workers.")
  st.write("- Provide clear and concise explanations of the PCP process and types of Work Pass.")
  st.write("- Utilize external data sources and user input to generate relevant information.")
  st.write("- Simplify understanding of informations for employers.")

  st.header("Feature")
  st.write("An AI assistant to help with user's enquiry on information regarding to PCP  and Work Pass.")

  st.header("Data sources")
  st.write("URL: https://www.mom.gov.sg/primary-care-plan/what-is-pcp")
  st.write("URL: https://www.mom.gov.sg/primary-care-plan/buying-a-pcp")
  st.write("URL: https://www.mom.gov.sg/primary-care-plan/getting-primary-care-services")
  st.write("URL: https://www.mom.gov.sg/passes-and-permits")
  
  st.header("Author")
  st.write("Tommy Loh")

def methodology():
  st.title("Methodology")
  st.header("Data flows")
  st.write(f""" \n
    1. The user interacts with the app interface (Streamlit), inputting a query into the text input area and submitting it to the backend for processing. \n
    2. The nature of the topic (PCP or Work Pass) is determined, and the website information extractor is called with the correct set of URLs. \n
    3. The context of the query is set based on the topic, including the query itself and the intended response format. \n
    4. The prompt is crafted appropriately to prevent prompt injection. \n
    5. The data is sent through the OpenAI API call, and the response is awaited. \n
    6. The retrieved response is displayed back to the app interface. \n\n
           """)
  st.image("Flowchart-Prompt-Engineering.png")
  st.header("Implementations")
  st.write(f""" \n
    - A my_script.py to have functions for extract information from websites, set context and create prompts, set environment configurations and to call OpenAI via API. \n
    - A ai_champion.py to create app interface, format and ordering of the pages. \n
    - Commit and push codes to GitHub, and have Streamlit create the app from GitHub files. \n
           """)

def primary_care_plan():
    st.title("MOM Primary Care Plan")
    # Input widget: Text area for user query
    user_query = st.text_area("Ask your question about Primary Care Plan:", height=100)

    # Output widget: Displaying the response
    if st.button("Submit"):
        assistant_res = get_completion(user_query)
        response = f"You asked: {user_query}. \n\n{assistant_res}"     
        st.write(response)

def work_passes():
    st.title("Work Passes")
    # Input widget: Text area for user query
    user_wp_query = st.text_area("Ask your question about work pass:", height=100)

    # Output widget: Displaying the response
    if st.button("Submit"):
        assistant_res = get_completion_workpass(user_wp_query)
        response = f"You asked: {user_wp_query}. \n\n{assistant_res}"      
        st.write(response)

page_names = ["About Us", "Methodology", "Primary Care Plan", "Work Passes"]
page_functions = [about_us, methodology, primary_care_plan, work_passes]

selected_page = st.sidebar.selectbox("Select a Page", page_names)

page_functions[page_names.index(selected_page)]()