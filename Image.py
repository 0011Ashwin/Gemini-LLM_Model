from dotenv import load_dotenv
## Loading all the environment variables
load_dotenv()

# importing all libraries
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

## Calling google api key from .env
genai.configure(api_key=os.getenv("API_KEY"))

# function to load Gemini Pro model getting response
model = genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input,image):
    # if input is not equal to blank 
    if input != "":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text


## initialize our streamlit app
st.set_page_config(page_title="Gemini Pro Vision", page_icon="🔮", layout="wide")

st.header("Gemini Application")
input = st.text_input("Input Prompt: ",key="input")

# File upload for vision-pro 
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
imgae=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Upload Image.",use_column_width=True)
    # image = uploaded_file.read()
    # st.image(image, caption='Uploaded Image.', use_column_width=True)
    # image = get_gemini_response(input,image)
    # st.image(image, caption='Generated Image.', use_column_width=True)


submit = st.button("Tell me about the iamge")

# if submit button is clicked
if submit:
    response = get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)





