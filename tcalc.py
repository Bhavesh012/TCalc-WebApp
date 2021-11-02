import sys
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from TCalc.tcalc import telescope, eyepiece, barlow_lens, focal_reducer
# sys.path.insert(0, 'home/amazing_bhavesh/Ubuntu/TCalc/TCalc')
# from tcalc import telescope, eyepiece, barlow_lens, focal_reducer
from streamlit.report_thread import REPORT_CONTEXT_ATTR_NAME
from threading import current_thread
from contextlib import contextmanager
from io import StringIO




@contextmanager
def st_redirect(src, dst):
    placeholder = st.empty()
    output_func = getattr(placeholder, dst)

    with StringIO() as buffer:
        old_write = src.write

        def new_write(b):
            if getattr(current_thread(), REPORT_CONTEXT_ATTR_NAME, None):
                buffer.write(b + '')
                output_func(buffer.getvalue() + '')
            else:
                old_write(b)

        try:
            src.write = new_write
            yield
        finally:
            src.write = old_write


@contextmanager
def st_stdout(dst):
    "this will show the prints"
    with st_redirect(sys.stdout, dst):
        yield


@contextmanager
def st_stderr(dst):
    "This will show the logging"
    with st_redirect(sys.stderr, dst):
        yield


st.title('TCalc: Telescope-Calculator')
# st.image('TCalc2.png', caption=None, width=50, use_column_width=None, clamp=False, channels='RGB', output_format='PNG')
'''
**TCalc** is a general toolkit designed for all the telescope owners and enthusiasts! 
This webapp has a set of functions that will allow you to calculate basic properties and performance of your telescope and eyepiece pair.
'''

with st.expander("About"):
    '''
    TCalc is built on the motive to spread awareness about telescopes and how to optimally use them in order to save time, money and sanity! Around 70% of amateur or rising astronomers and telescope owners waste 65% of their savings on buying the wrong or incompatible stuff for their telescope. 90% of them deals with high-level of frustration when trying their eyepieces or barlows.

    With TCalc, we will be aiming to put this to an end! TCalc package provides the functionality to estimate 95% of the information about their telescope, and it's with just three parameters, aperture and focal length of telescope and eyepiece. With the input, the package will output all the information like maximum usable magnification, the smallest eyepiece that you can use and many more things such as focal-ratio, limiting magnitude, resolution power, etc. In TCalc, you can even create profiles of your telescope and eyepieces to simulate them in different ways. For advanced users, TCalc provides plots of resolution performance, eyepiece statistics for more detailed planning of their observations.

    TCalc is written in Python and is compatible with every OS. It even works on phones too. TCalc package was pursued as a part of [Code/Astro Workshop 2021](https://semaphorep.github.io/codeastro/) by group 9. The authors of this package are: 


    |Members|Bhavesh Rajpoot|Ryan Keenan|Binod Bhattarai|Dylon Benton|
    |-----|-----|----|----|-----|

    ## Attribution

    Please cite the DOI if you make use of this software in your research.
    [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5035311.svg)](https://doi.org/10.5281/zenodo.5035311)
    '''


''' Let's start! '''

# with st.sidebar:
# ''' Enter the details of the telescope whose details you want to know.'''

# Dia_o = st.number_input('Telescope Aperture Size (in mm)', value=203.2, step=0.1)
# fl_o = st.number_input('Focal Length of Objective (in mm)', value=2032, step=1)
# user_age = st.number_input('User Age (optional)', value=22, step=1, format='%d')

# fl_e = st.number_input('Focal Length of Eyepiece (in mm)', value=25, step=1)
# FOV_e = st.number_input('FOV of Eyepiece', value=50, step=0.1)

# '''Selected Inputs:'''

col1, col2 = st.columns([2,1])

with col1:
    st.subheader("Enter the details of the telescope whose details you want to know.")
    Dia_o = st.number_input('Telescope Aperture Size (in mm)', value=203.2, step=0.1)
    fl_o = st.number_input('Focal Length of Objective (in mm)', value=2032, step=1)
    user_age = st.number_input('User Age (optional)', value=22, step=1, format='%d')
    
with col2:
    st.subheader("Selected Inputs:")
    st.write('Diameter of Objective:', Dia_o , 'mm')
    st.write('Focal Length of Objective', fl_o , 'mm')
    st.write("User's Age", user_age , 'yrs')
# with col3:
    # st.subheader("A narrow column with the data")

# st.write('Diameter of Objective:', Dia_o , 'mm')
# st.write('Focal Length of Objective', fl_o , 'mm')
# st.write("User's Age", user_age , 'yrs')
# '''
# |Param|Value|Unit|
# |-----|-----|----|
# |D_o|{{Dia_o}}|mm|
# |f_o|{{fl_o}}|mm|

# '''

# st.markdown('''
#     |Param|Value|Unit|
#     |-----|-----|----|
#     |D_o|{{Dia_o}}|mm|
# ''')

ota = telescope(D_o=Dia_o, f_o=fl_o, user_D_eye=None, user_age=user_age) # adding configuration of 8in scope

omni_40 = eyepiece(f_e = 40, fov_e = 52) # defining 40 mm eyepiece
omni_25 = eyepiece(f_e = 25, fov_e = 52) # defining 25 mm eyepiece

# adding eyepiece to the telescope
ota.add_eyepiece(omni_40, id='omni_40', select=True)
ota.add_eyepiece(omni_25, id='omni_25', select=True)

# adding additional optical parts
reducer = focal_reducer(.5) # defining focal reducer of 0.5x
barlow = barlow_lens(2)     # defining barlow lens of 2x

ota.add_optic(reducer,'reducer 1', select=False) # adding reducer to the telescope
ota.add_optic(barlow,'barlow 1', select=False)    # adding barlow to the telescope



# listing all the added eyepieces in a table format
# if st.button('List Eyepiece'):
with st.expander("List of Eyepiece and other optics", expanded = True):
    with st_stdout("code"), st_stderr("code"):
        ota.list_eyepiece()

# listing overall configuration of the telescope in expanded format
if st.button('Show Configuration'):
    with st.expander("Output", expanded = True):
        with st_stdout("code"), st_stderr("code"):
            ota.say_configuration()







# st.download_button('On the dl', data)
# st.checkbox('Check me out')
# st.radio('Radio', [1,2,3])
# st.selectbox('Select', [1,2,3])
# st.multiselect('Multiselect', [1,2,3])
# st.slider('Slide me', min_value=0, max_value=10)
# st.select_slider('Slide to select', options=[1,'2'])

