import streamlit as st

st.title("Basic Calculator")

num1 = (st.number_input("Enter the first number", step=1, format="%d"))    
num2 = (st.number_input("Enter the second number", step=1, format="%d")) 
operation = st.selectbox("Select an operation", ["Addition", "Subtraction", "Multiplication", "Division"])  
result = None   
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero!")
    
    if result is not None:
        st.success(f"The result of {operation} is: {result}")
