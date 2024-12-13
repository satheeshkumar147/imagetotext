import streamlit as st
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
import os

from PIL import Image
import pathlib
import textwrap

# Configure the Key

genai.configure(api_key = os.getenv('GOOGLE_API_KEY ')) 

# Page for Image to Text

st.header("Gemini Image to Text Application")
input = st.text_input("Input Prompt: ", key = "input")
uploaded_img = st.file_uploader("Upload the Image...", type = ["jpg", "png","jpeg"])



# Display the Image

image = ""

if uploaded_img is not None:
    image = Image.open(uploaded_img)
    st.image(image, caption = "Image Uploaded",
             use_column_width = True)
    
def get_gemini_response(input, image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    if input!="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(input)
    return response.text
    
submit = st.button("Submit")

if submit:
    response = get_gemini_response(input, image)
    st.subheader("The Response is")
    st.write(response)
    

    