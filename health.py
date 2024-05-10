import streamlit as st
import google.generativeai as genai
from PIL import Image

apikey="AIzaSyAZXd4Q_48TqdZhUz9M_S_NzEf6qbar3Io"

genai.configure(api_key=apikey)
model = genai.GenerativeModel('gemini-pro-vision')

def get_response(input,image,prompt):
    response = model.generate_content([input , image[0] , prompt])
    return response.text

def image_setup (imagefile):
    if imagefile is not None :
        bytes_data = imagefile.getvalue()

        image_parts = [{
            "mime_type" : imagefile.type,
            "data" : bytes_data
        }]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    

# to handle frontend
st.set_page_config(page_title="Health Expert")
st.header("Ask Your Health expert Sabari")
input=st.text_input("Input: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file:
    image = uploaded_file

# Display the image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True ,width=200)

submit = st.button("Ask the question")

inputprompt = """ your a health expert  and nutritionist  you need to see the food items from the image and calculate the
total calories also provide the details of every food as below format
 1. Item 1 - no of calories
 2. Item 2 - no of calories
 -------------------------
 total calories intake
"""

if submit:
    if uploaded_file :
        image_data = image_setup(uploaded_file)

        response = get_response(inputprompt , image_data, input)

        st.subheader("Response")
        st.write(response)
    else :
        st.subheader("Response")
        st.write("Sorry I can't get it , Please come again .")
