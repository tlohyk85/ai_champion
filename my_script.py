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

# This is a function that send input (i.e., prompt) to LLM and receive the output from the LLM
def get_completion(user_input):
    url = "https://www.mom.gov.sg/primary-care-plan/what-is-pcp"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    final_text = soup.text.replace('\n', '')
    prompt = f"""
        Data source website: https://www.mom.gov.sg/primary-care-plan/what-is-pcp.
        This website is about Primary Care Plan (PCP) introduced by the Ministry of Manpower.
        The text delimited by triple backticks are scraped from the website and parsed using `html.parser`.
        Please answer the user's enquiry about the PCP in a professional and informative manner. If applicable, include guiding steps in your response.
        ```
        {final_text}
        ```
        """
    model="gpt-4o-mini"
    response = client.chat.completions.create(
        model=model,
        messages = [{"role": "system", "content": prompt},
                    {"role": "user", "content": user_input}],
        temperature=0, # this is the degree of randomness of the model's output
        top_p=1.0,
        max_tokens=4096,
        n=1
    )
    return response.choices[0].message.content






""" user_input = "What is this PCP? Do I need it? And how can I apply it?"
len(final_text.split())


# This example shows the use of angled brackets <> as the delimiters

response = get_completion(prompt, user_input)
print(response) """

