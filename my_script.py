import os
from dotenv import load_dotenv
from openai import OpenAI
from getpass import getpass
from bs4 import BeautifulSoup
import requests
import urllib3 
import tiktoken

load_dotenv('.env')
mykey= os.getenv("OPENAPI_API_KEY")
client = OpenAI(api_key=mykey)

def fetch_and_parse_urls(urls):
    results = []
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for error HTTP statuses
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract the desired text from the HTML, adjust the selector as needed
            text = soup.text.replace('\n', '')
            results.append(text)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            results.append(f"Error fetching {url}")

    return results

pcp_urls = [
    "https://www.mom.gov.sg/primary-care-plan/what-is-pcp",
    "https://www.mom.gov.sg/primary-care-plan/buying-a-pcp",
    "https://www.mom.gov.sg/primary-care-plan/getting-primary-care-services"
]


# This is a function that send input (i.e., prompt) to LLM and receive the output from the LLM
def get_completion(user_input):
    final_text = fetch_and_parse_urls(pcp_urls)
    prompt = f"""
        This data source of the website is about Primary Care Plan (PCP) introduced by the Ministry of Manpower.
        The text delimited by triple backticks are scraped from the website and parsed using `html.parser`.
        Please answer the user's enquiry about the PCP in a professional and informative manner. If applicable, include guiding steps in your response.
        ```
        {final_text}
        ```
        """
    user_prompt = f"""
        The text by quadruple backticks is the user inputs:
        ````
        {user_input}
        ````
    """
    model="gpt-4o-mini"
    response = client.chat.completions.create(
        model=model,
        messages = [{"role": "system", "content": prompt},
                    {"role": "user", "content": user_prompt}],
        temperature=0, # this is the degree of randomness of the model's output
        top_p=1.0,
        max_tokens=4096,
        n=1
    )
    return response.choices[0].message.content

workpass_urls = [
    "https://www.mom.gov.sg/passes-and-permits"
]

# This is a function that send input (i.e., prompt) to LLM and receive the output from the LLM
def get_completion_workpass(user_input):
    final_text = fetch_and_parse_urls(workpass_urls)
    prompt = f"""
        This data source of the website is about work passes introduced by the Ministry of Manpower.
        The text delimited by triple backticks are scraped from the website and parsed using `html.parser`.
        Please answer the user's enquiry about the work passes in a professional and informative manner. If applicable, include guiding steps in your response.
        ```
        {final_text}
        ```
        """
    user_prompt = f"""
        The text by quadruple backticks is the user inputs:
        ````
        {user_input}
        ````
    """
    model="gpt-4o-mini"
    response = client.chat.completions.create(
        model=model,
        messages = [{"role": "system", "content": prompt},
                    {"role": "user", "content": user_prompt}],
        temperature=0, # this is the degree of randomness of the model's output
        top_p=1.0,
        max_tokens=4096,
        n=1
    )
    return response.choices[0].message.content


