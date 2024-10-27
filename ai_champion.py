import streamlit as st
import pandas as pd
import numpy as np
from my_script import get_completion

def about_us():
  st.title("About Us")
  st.write("This application aims to empower users with information regarding the Primary Care Plan (PCP) for foreign workers in Singapore. We leverage external data sources, user input, and advanced language processing to deliver accurate and helpful insights.")
  
  st.header("Objectives")
  st.write("- Assist users with inquiries related to the PCP for foreign workers.")
  st.write("- Provide clear and concise explanations of the PCP process.")
  st.write("- Utilize external data sources and user input to generate relevant information.")
  st.write("- Simplify understanding of the PCP for employers.")

  st.header("Feature")
  st.write("An AI assistant to help with user's enquiry.")

  st.header("Data sources")
  st.write("URL: https://www.mom.gov.sg/primary-care-plan/what-is-pcp")

def methodology():
  st.title("Methodology")
  st.write("This is the Methodology page.")

def primary_care_plan():
    st.title("MOM Primary Care Plan")
    # Input widget: Text area for user query
    user_query = st.text_area("Ask your question about Primary Care Plan:", height=100)

    # Output widget: Displaying the response
    if st.button("Submit"):
        # You can use a language model like GPT-3 to generate a response based on the user query and the website content
        # Here's a simplified example:
        assistant_res = get_completion(user_query)
        response = f"You asked: {user_query}. \n\n{assistant_res}"  # Replace with actual response generation logic    
        st.write(response)

def about_mom():
  st.title("About MOM")
  st.write("This is the About MOM page.")

page_names = ["About Us", "Methodology", "Primary Care Plan", "About MOM"]
page_functions = [about_us, methodology, primary_care_plan, about_mom]

selected_page = st.sidebar.selectbox("Select a Page", page_names)

page_functions[page_names.index(selected_page)]()