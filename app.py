import streamlit as st

def largest_number(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

st.title("Largest Number Finder")

st.write("This app helps you find the largest number among three given numbers.")

num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")
num3 = st.number_input("Enter the third number")

if st.button("Find largest number"):
    result = largest_number(num1,num2,num3)
    st.write(f"The largest number among {num1}, {num2}, and {num3} is {result}.")
