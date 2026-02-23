import streamlit as st

st.markdown("""
<style>

/* Page background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* Title styling */
h1 {
    text-align: center;
    color: #38bdf8;
    font-family: Arial;
}

/* Input box */
.stTextInput > div > div > input {
    border-radius: 10px;
    padding: 10px;
    border: 2px solid #38bdf8;
}

/* Button styling */
.stButton > button {
    background-color: #38bdf8;
    color: black;
    border-radius: 10px;
    height: 45px;
    width: 100%;
    font-weight: bold;
    transition: 0.3s;
}

/* Button hover */
.stButton > button:hover {
    background-color: #0ea5e9;
    color: white;
}

/* Chat message box */
.chat-box {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 12px;
    margin-top: 15px;
    border-left: 5px solid #38bdf8;
}

</style>
""", unsafe_allow_html=True)

st.title("Simple Chatbot")

Question = st.text_input("Ask me anything!")

if st.button("Send"):
    st.write(f"You asked:",Question)
    st.write("Sorry, I am just a simple chatbot and cannot answer your question yet.")