import streamlit as st

st.write("# Biggest among three numbers")

def display(num):
  st.subheader('The biggest number is {}'.format(num))

def compare(x,y,z):
  if(x>y and x>z):
    display(x)
  elif(y>z):
    display(y)
  else:
    display(z)


num1 = st.number_input("First Number",step=1)
num2 = st.number_input("Second Number",step=1)
num3 = st.number_input("Third Number",step=1)

compare(num1,num2,num3)
