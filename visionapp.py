import streamlit as st
import google.generativeai as genai
from PIL import Image

apikey="Use_Your_Apikey"

genai.configure(api_key=apikey)
model = genai.GenerativeModel('gemini-pro-vision')

def get_response(input , image):
    if not image:
        return "I can't get you please come again"
    if input != "":
        response = model.generate_content([input , image])
    else :
        response = model.generate_content(image)

    try:
        return response.text
    except Exception as e:
        return "Sorry , The question is too sensitive."
    

# to handle frontend
st.set_page_config(page_title="Vision Ai")
st.header("I can see you")
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


if submit:
   st.write("Please wait and give some time to sabari to recall")


if submit :

    res = get_response(input, image) or None
    st.subheader("Response")
    if res:
        st.write(res)
    else:
        st.subheader("Your Questions may senstive ")

