"""Home page shown when the user enters the application"""
import streamlit as st

def write():
    #defining page font styles
    st.markdown(
        """
        <style>
        html, body, [class*="css"]  {
        font-family:"Bahnschrift", sans-serif;
        }
        .standard_text{font-size: 16px;}
        </style>
        """, unsafe_allow_html=True)
    # with st.spinner("Loading About ..."):
    st.markdown('''
    ## Contributions

    This an open source project and you are very welcome to **contribute** your awesome
    comments, questions, resources and apps as
    [issues](https://github.com/Bhavesh012/TCalc-WebApp/issues) or
    [pull requests](https://github.com/Bhavesh012/TCalc-WebApp/pulls)
    to the [source code](https://github.com/Bhavesh012/TCalc-WebApp).


    ## The Developer

    This project is developed by Bhavesh Rajpoot. You can learn more about me at
    [bhaveshrajpoot.com](https://www.bhaveshrajpoot.com).

    Feel free to reach out if you wan't to join the project as a developer. Here is my email id: *rajputbhavesh04@gmail.com*.
    ''', unsafe_allow_html=True)