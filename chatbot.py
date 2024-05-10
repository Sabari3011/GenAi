import streamlit as st
import google.generativeai as genai

apikey="AIzaSyAZXd4Q_48TqdZhUz9M_S_NzEf6qbar3Io"

genai.configure(api_key=apikey)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_response(q):
    response = chat.send_message(q,stream=True)
    return response

st.set_page_config(page_title="Chatbot")

st.header("Chat with Sabari")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []




input = st.text_input("Type Message: ",key="input")

submit = st.button("send")

if submit and input :
    response = get_response(input)
    st.session_state['chat_history'].append(("You",input))
    st.subheader("Response")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Sabari",chunk.text))

st.subheader("Chat History")

for role , text in st.session_state["chat_history"]:
    if role == "You" :
        st.write(f"""
        <div style="margin-left: auto; margin-bottom : 2% ;
         width: 50%; background-color: #97f0ed; color : black ; padding: 10px;">
        {role} : {text}
        </div>
        """,unsafe_allow_html=True)
    else:
        st.write(f"""
        <div style="margin-right: auto;margin-bottom : 2% ; width: 50%; background-color: #f5bb84; color : black ; padding: 10px;">
        {role} : {text}
        </div>
        """,unsafe_allow_html=True)

    

