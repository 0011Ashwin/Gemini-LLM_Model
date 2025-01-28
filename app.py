from dotenv import load_dotenv
## loading all the environment variables
load_dotenv()

# importing all libraries
import streamlit as st
import os
import google.generativeai as genai

## calling google api key from .env
genai.configure(api_key=os.getenv("API_KEY"))


## function to load gemini model and getting response
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

## initialize our streamlit app
## header part of web-page & text box
st.header("Gemini Application Flash 2.O Exp")
st.subheader("Powered by Ashwin Mehta")

## Taking input from user from user 
input = st.text_input("Input: ", key="input")
submit = st.button("Ask the Question")




## When submit is clicked
if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
    
    

    
    

