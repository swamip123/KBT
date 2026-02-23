import streamlit as st

# ---------- CSS ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#0f172a,#1e293b);
    color: white;
}

h1 {
    text-align: center;
    color: #38bdf8;
}

div[data-testid="stForm"] {
    background-color: #1e293b;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.4);
}

.stButton > button {
    background-color: #38bdf8;
    color: black;
    border-radius: 8px;
    width: 100%;
    height: 45px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #0ea5e9;
    color: white;
}
</style>
""", unsafe_allow_html=True)


st.title("📋 User Information Form")


with st.form("user_form"):

    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    age = st.number_input("Age", min_value=1, max_value=100)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    message = st.text_area("Your Message")

    submit = st.form_submit_button("Submit")

if submit:
    st.success("✅ Form Submitted Successfully!")

    st.write("### Submitted Details")
    st.write("Name:", name)
    st.write("Email:", email)
    st.write("Age:", age)
    st.write("Gender:", gender)
    st.write("Message:", message)

