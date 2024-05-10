import streamlit as st
import google.generativeai as genai


apikey="AIzaSyAZXd4Q_48TqdZhUz9M_S_NzEf6qbar3Io"

genai.configure(api_key=apikey)
model = genai.GenerativeModel('gemini-pro')

#function to get response from ai
def get_response(q):
    if q == "" or len(q) < 3:
        return "I can't get you please come again"
    response = model.generate_content(q)
    try:
        return response.text
    except Exception as e:
        return "Sorry , The question is too sensitive."
     

# to handle frontend
st.set_page_config(page_title="Gen Ai")
st.header("Ask anything to Sabari")
input=st.text_input("Input: ",key="input")
submit = st.button("Ask the question")

if submit:
   st.write("Please wait and give some time to sabari to recall")


if submit :

    res = get_response(input) or None
    st.subheader("Response")
    if res:
        st.write(res)
    else:
        st.subheader("Your Questions may senstive ")

