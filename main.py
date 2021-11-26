"""Main module for the streamlit app"""
import streamlit as st

from src.Pages import home, tcalc, doc, about

from multiapp import MultiApp


app = MultiApp()

# setting page configuration
st.set_page_config(
    page_title='TCalc: Telescope-Calculator',
    page_icon='https://github.com/Bhavesh012/TCalc/blob/main/TCalc2.png',
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        # 'Get Help': 'https://www.extremelycoolapp.com/help',
        # 'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': '''
        **TCalc** is a general toolkit designed for all the telescope owners and enthusiasts! 
        This webapp has a set of functions that will allow you to calculate basic properties and performance of your telescope and eyepiece pair.
        '''
    }
)

# Add all your application here
app.add_app("Home", home.write)
app.add_app("TCalc", tcalc.write)
app.add_app("Telescope Basics", doc.write)
app.add_app("About", about.write)

# The main app
app.run()

st.sidebar.title("Navigation")

st.sidebar.title("Contribute")
st.sidebar.info(
    "This an open source project and you are very welcome to **contribute** your awesome "
    "comments, questions, resources and apps as "
    "[issues](https://github.com/Bhavesh012/TCalc-WebApp/issues) of or "
    "[pull requests](https://github.com/Bhavesh012/TCalc-WebApp/pulls) "
    "to the [source code](https://github.com/Bhavesh012/TCalc-WebApp). "
)

st.sidebar.title("About")
st.sidebar.info(
    """
    This app is maintained by Bhavesh Rajpoot and is based on TCalc package. You can learn more about me at
    [bhaveshrajpoot.com](https://www.bhaveshrajpoot.com).
    """)

