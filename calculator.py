import streamlit as st
st.title("Calculator")

# taking the input
num1=st.number_input("Enter the number 1")
num2=st.number_input("Enter the number 2")

selection=st.selectbox("Select",['Add','Substract','Multipliction','Division'])
result=None
if st.button("Submit"):
    if selection=='Add':
        result=num1+num2
    elif selection == 'Substract':
        result=num1-num2
    elif selection == 'Multipliction':
        result=num1*num2
    elif selection=='Division':
        result =num1/num2
    else:
        result=None

if result:
    st.success(f"Result: {result}")
