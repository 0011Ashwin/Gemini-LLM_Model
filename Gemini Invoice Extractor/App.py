from dotenv import load_dotenv

## Load all the environment variables from the .env file
load_dotenv()

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# getting the API from GOOGLE_API_KEY
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

## Function to load Gemini Pro vision
model = genai.GenerativeModel('gemini-pro')

# input -> what have to  do
# prompt -> what message i want display
def get_gemini_response(input,image,prompt):
    response = model.generate_content([input,image[0],prompt])
    return response.text

## initialize our streamlit app 
st.set_page_config(page_title="Gemini MultiLanguage Invoice Extractor", page_icon="🧊", layout="centered", initial_sidebar_state="expanded")
st.header("Gemini Invoice Extractor")
input = st.text_input("Input Prompt: ",key="input")
upload_file = st.file_uploader("Choose an image....", type=["jpg", "png", "jpeg"], key="image")

