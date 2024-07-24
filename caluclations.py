import streamlit as st
st.title("Prime or not")
a = st.text_input(label="Enter the term number (n)")

if st.button("Submit"):
    try:
        num = int(a)
        count =0
        for i in range(1,num+1):
            if num % i == 0:
                count +=1
        if count ==2:
            st.write("Prime number")
        else:
            st.write("Not a prime number")
    except ValueError:
        st.write("Please enter a valid number (positive integer)")