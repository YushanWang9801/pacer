"""
Author: Yushan Wang
Date: 2024-06-20

Description: A Streamlit application for LLM prototype 
to provide detailed information about parks and trails using 
the National Park Service API and OpenAI's GPT model.
"""

import requests
import streamlit as st
from openai import OpenAI
from decouple import config
from langchain.prompts import PromptTemplate


from utils import prompt_template
from utils import INIT_PROMPT, API_BASE_URL, CHAT_INPUT_PROMPT, MAX_TOKEN
from utils import fetch_park_info

NPS_API_KEY = config('NPS_API_KEY')
OPENAI_API_KEY = config('OPENAI_API_KEY')

client = OpenAI(
    base_url= API_BASE_URL,
    api_key= OPENAI_API_KEY
)


st.set_page_config(
    page_title="Custom Park Trail GPT",
    page_icon="🏞️",
    layout="wide"
)

st.title("Custom Park Trail GPT")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", 
         "content": INIT_PROMPT}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_prompt = st.chat_input(CHAT_INPUT_PROMPT)

if user_prompt:
    st.session_state.messages.append({"role": "user", 
                                      "content": user_prompt})
    
    with st.chat_message("user"):
        st.write(user_prompt)
    
    real_time_info = fetch_park_info(user_prompt)

    chat_history = "\n".join([
        f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages
        ])
    
    prompt = prompt_template.format(chat_history=chat_history, 
                                    question=user_prompt, 
                                    real_time_info=real_time_info)
    # print(prompt)
    
    try:

        response = client.chat.completions.create(
            model= "gpt-4o",
            messages=[
                {"role": "user", 
                 "content": prompt}
            ],
            max_tokens= MAX_TOKEN
        )
        gpt_response = response.choices[0].message.content

    except Exception as e:
        gpt_response = f"Error generating response: {e}"
    
    st.session_state.messages.append({"role": "assistant", 
                                      "content": gpt_response})
    
    with st.chat_message("assistant"):
        st.write(gpt_response)
