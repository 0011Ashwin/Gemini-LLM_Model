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

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        
        image_parts =[
            {
                "mime_type": uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    

## initialize our streamlit app 
st.set_page_config(page_title="Gemini MultiLanguage Invoice Extractor", page_icon="🧊", layout="centered", initial_sidebar_state="expanded")
st.header("Gemini Invoice Extractor")
input = st.text_input("Input Prompt: ",key="input")
upload_file = st.file_uploader("Choose an image of the invoice....", type=["jpg", "png", "jpeg"])
image=""
if upload_file is not None:
    image = Image.open(upload_file)
    # Also want to upload this image
    st.image(image, caption="Upload Image.", use_column_width=True)
    
submit  = st.button("Tell me about the invoice")

input_prompt = """
You are an expert in understanding invoices. we will upload a image as invoice
and you will have to answer any question based on the uploaded invocies image
"""
# If submit button clicked 
if submit:
    image_data = input_image_details(upload_file)
    response = get_gemini_response(input_prompt,image_data,input)
    st.subheader("The response is")
    st.write(response)