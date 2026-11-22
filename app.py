import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen

def main():
    
    st.header("AI Based Attendance System")
    name = st.text_input("Enter your name:")
    if st.button("Submit",type= 'primary' ,key="btn1",):
        print(f"Hello, {name}!")

main()