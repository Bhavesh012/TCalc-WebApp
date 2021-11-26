"""Home page shown when the user enters the application"""
import streamlit as st

# pylint: disable=line-too-long
def write():
    
    with st.spinner("Loading Home ..."):
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

        #Title
        st.title('TCalc: Telescope-Calculator')

        #Logo
        # st.image('TCalc2.png', caption=None, width=50, use_column_width=None, clamp=False, channels='RGB', output_format='PNG')

        #Basic intro
        st.markdown('''<p style="font-family:Cambria;font-size:20px;">
                    TCalc is a general toolkit designed for all the telescope owners and enthusiasts! 
                    This webapp has a set of functions that will allow you to calculate basic properties and performance of your telescope and eyepiece pair.
                    </p>''', unsafe_allow_html=True)

        #About
        with st.expander("About"):
            st.markdown('''
            TCalc is built on the motive to spread awareness about telescopes and how to optimally use them in order to save time, money and sanity! Around 70% of amateur or rising astronomers and telescope owners waste 65% of their savings on buying the wrong or incompatible stuff for their telescope. 90% of them deals with high-level of frustration when trying their eyepieces or barlows.

            With TCalc, we will be aiming to put this to an end! TCalc package provides the functionality to estimate 95% of the information about their telescope, and it's with just three parameters, aperture and focal length of telescope and eyepiece. With the input, the package will output all the information like maximum usable magnification, the smallest eyepiece that you can use and many more things such as focal-ratio, limiting magnitude, resolution power, etc. In TCalc, you can even create profiles of your telescope and eyepieces to simulate them in different ways. For advanced users, TCalc provides plots of resolution performance, eyepiece statistics for more detailed planning of their observations.

            TCalc is written in Python and is compatible with every OS. It even works on phones too. TCalc package was pursued as a part of [Code/Astro Workshop 2021](https://semaphorep.github.io/codeastro/) by group 9. The authors of this package are: 


            |Members|Bhavesh Rajpoot|Ryan Keenan|Binod Bhattarai|Dylon Benton|
            |-----|-----|----|----|-----|

            ## Attribution

            Please cite the DOI if you make use of this software in your research.
            [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5035311.svg)](https://doi.org/10.5281/zenodo.5035311)
            ''', unsafe_allow_html=True)
