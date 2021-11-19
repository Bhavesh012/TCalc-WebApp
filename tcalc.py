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
import datetime
import time
import streamlit.components.v1 as components  # Import Streamlit

# text styling using CSS 
# st.markdown('''<p style="
#             font-family:Bahnschrift;
#             font-size: 50px;
#             font_style:;
#             font-weight:;
#             letter-spacing:;
#             font-stretch:;
#             color:;
#             background-color:;
#             text-align:center;
#             font-variant:;
#             text-transform:;
#             text-indent:;
#             ">Let's start!
#             </p>''', unsafe_allow_html=True) 

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

st.markdown(
    """
    <style>
    html, body, [class*="css"]  {
    font-family:"Bahnschrift", sans-serif;
    }
    .standard_text{font-size: 16px;}
    </style>
    """, unsafe_allow_html=True)

st.title('TCalc: Telescope-Calculator')
# st.image('TCalc2.png', caption=None, width=50, use_column_width=None, clamp=False, channels='RGB', output_format='PNG')
st.markdown('''<p style="font-family:Cambria;font-size:20px;">
            TCalc is a general toolkit designed for all the telescope owners and enthusiasts! 
            This webapp has a set of functions that will allow you to calculate basic properties and performance of your telescope and eyepiece pair.
            </p>''', unsafe_allow_html=True)

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

# Render the h1 block, contained in a frame of size 200x200.
# components.iframe("https://docs.streamlit.io/en/latest")
st.markdown('''<p style="
            font-family:Bahnschrift;
            font-size: 50px;
            text-align:center;
            ">Let's start!
            </p>''', unsafe_allow_html=True) 

col1, col2, col3 = st.columns([1,1,2])

with col1: #column for entering details of OTA
    st.subheader("Enter the details of the telescope whose details you want to know.")
    Dia_o = st.number_input('Telescope Aperture Size (in mm)', value=203.2, step=1.0, format='%f')   #ota dia
    fl_o = st.number_input('Focal Length of Objective (in mm)', value=2032, step=1)     #ota fl
    user_age = st.number_input('User Age (optional)', value=22, step=1, format='%d')    #user age

with col2: #shows the selected inputs
    st.subheader("Selected Inputs:")
    # st.write('Diameter of Objective:', Dia_o , 'mm')
    # st.write('Focal Length of Objective:', fl_o , 'mm')
    # st.write("User's Age:", user_age , 'yrs')
    st.markdown(
    f'''
    |Aperture|Focal Length|User's Age|
    |-|-|-|
    |``{Dia_o}`` mm|``{fl_o}`` mm|``{user_age}`` yrs|
    ''', unsafe_allow_html=True)

tel_type = ('Refractor (Diotropics)', 'Reflector (Catatropics)', 'Catadiotropics')
dio_type = ('Galiliean', 'Achromatic', 'Apochromatic', 'Superachromat')
cata_type = ('Gregorian', 'Newtonian', 'Nasmyth', 'Ritchey–Chrétien', 'Three-mirror Anastigmat')
catadio_type = ('Schmidt-Cassegrain', 'Maksutov-Cassegrain', 'Corrected Dall-Krikham')
with col3: #shows diagram of telescope
    st.subheader("Telescope Diagrams")
    ota_type = st.radio('Choose your telescope type', tel_type)

    if ota_type == tel_type[0]: #diotropics
        st.markdown('Uses _Lenses_')
        st.selectbox('Select Sub-type', dio_type)
    if ota_type == tel_type[1]: #catatropics
        st.markdown('Uses _Mirrors_')
        st.selectbox('Select Sub-type', cata_type)  
    if ota_type == tel_type[2]: #catadiotropics
        st.markdown('Uses both _Lenses_ and _Mirrors_')
        st.selectbox('Select Sub-type', catadio_type)


ota = telescope(D_o=Dia_o, f_o=fl_o, user_D_eye=None, user_age=user_age) # adding configuration of 8in scope
st.markdown("""---""") #adding divider
st.subheader("Adding Optical Components")

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: space-evenly;} </style>', unsafe_allow_html=True)
# st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{padding-left:2px;}</style>', unsafe_allow_html=True)

with st.expander('Eyepiece', expanded = True):
    col3, col4, col5 = st.columns([1,1,1])
    with col3: #adding input panel for eyepiece 1
        st.markdown('<p style="font-family:Bahnschrift; font-size: 20px;">Eyepiece 1</p>', unsafe_allow_html=True)
        fl_e_1 = st.number_input('Focal Length of Eyepiece (in mm)', value=25, step=1, key='ep_1')  #focal length of eyepiece 
        fov_ep_1 = st.number_input('FOV of eyepiece (in deg)', value=50, step=1, key='ep_1')        #fov of eyepiece 
        name_e_1 = st.text_input('Define id of eyepiece', value="25mm Plössl", key='ep_1')          #name id of eyepiece
        select_e_1 = False   
        # if st.checkbox(f'Add {name_e_1}'):
        #     select_e_1 = True
        #     st.markdown("Eyepiece Selected = _True_")
        #     with st_stdout("code"), st_stderr("code"):
        #         ota.add_eyepiece(eyepiece(f_e = fl_e_1, fov_e = fov_ep_1), id=name_e_1, select=select_e_1)

    with col4: #adding input panel for eyepiece 2
        st.markdown('<p style="font-family:Bahnschrift; font-size: 20px;">Eyepiece 2</p>', unsafe_allow_html=True)
        fl_e_2 = st.number_input('Focal Length of Eyepiece (in mm)', value=6, step=1,key='ep_2')
        fov_ep_2 = st.number_input('FOV of eyepiece (in deg)', value=50, step=1, key='ep_2')
        name_e_2 = st.text_input('Define id of eyepiece', value="6mm Kellner", key='ep_2')
        select_e_2 = False   
        # if st.checkbox(f'Add {name_e_2}'):
        #     select_e_2 = True
        #     st.markdown("Eyepiece Selected = _True_")
        #     with st_stdout("code"), st_stderr("code"):
        #         ota.add_eyepiece(eyepiece(f_e = fl_e_2, fov_e = fov_ep_2), id=name_e_2, select=select_e_2)

    with col5: #adding input panel for eyepiece 3
        st.markdown('<p style="font-family:Bahnschrift; font-size: 20px;">Eyepiece 3</p>', unsafe_allow_html=True)
        fl_e_3 = st.number_input('Focal Length of Eyepiece (in mm)', value=40, step=1, key='ep_3')
        fov_ep_3 = st.number_input('FOV of eyepiece (in deg)', value=52, step=1, key='ep_3')
        name_e_3 = st.text_input('Define id of eyepiece', value="40mm Omni", key='ep_3')
        select_e_3 = False   
        # if st.checkbox(f'Add {name_e_3}'):
        #     select_e_3 = True
        #     st.markdown("Eyepiece Selected = _True_")
        #     with st_stdout("code"), st_stderr("code"):
        #         ota.add_eyepiece(eyepiece(f_e = fl_e_3, fov_e = fov_ep_3), id=name_e_3, select=select_e_3)
    
    eyepiece = st.radio('Choose the Eyepiece', [f'{name_e_1} Eyepiece', f'{name_e_2} Eyepiece', f'{name_e_3} Eyepiece'])
    if eyepiece == f'Add {name_e_1}':
        select_e_1 = True
        st.markdown("Eyepiece Selected = _True_")
        with st_stdout("code"), st_stderr("code"):
            ota.add_eyepiece(eyepiece(f_e = fl_e_1, fov_e = fov_ep_1), id=name_e_1, select=select_e_1)
    elif eyepiece == f'Add {name_e_2}':
        select_e_2 = True
        st.markdown("Eyepiece Selected = _True_")
        with st_stdout("code"), st_stderr("code"):
            ota.add_eyepiece(eyepiece(f_e = fl_e_2, fov_e = fov_ep_2), id=name_e_2, select=select_e_2)
    elif eyepiece == f'Add {name_e_3}':
        select_e_3 = True
        st.markdown("Eyepiece Selected = _True_")
        with st_stdout("code"), st_stderr("code"):
            ota.add_eyepiece(eyepiece(f_e = fl_e_3, fov_e = fov_ep_3), id=name_e_3, select=select_e_3)
with st.expander("Barlows", expanded = False):
    col6, col7, col8 = st.columns([1,1,1])
    with col6:
        st.markdown("**Barlow 1**")
        factor_1 = st.number_input('Barlow Factor', min_value=1.0, value=2.0, step=1.0, format='%f', key='bar_1')
        name_barlow_1 = st.text_input('Define id of Barlow', value="2x", key='bar_1')
        select_barlow_1 = False
        # if st.checkbox(f'Add {name_barlow_1} Barlow'):
        #     select_barlow_1 = True
        #     st.markdown("Barlow Selected = _True_")
        #     with st_stdout("code"), st_stderr("code"):
        #         ota.add_optic(barlow_lens(barlow=factor_1), name_barlow_1, select=select_barlow_1)

    with col7:
        st.markdown("**Barlow 2**")
        factor_2 = st.number_input('Barlow Factor', min_value=1.0, value=3.0, step=1.0, format='%f', key='bar_2')
        name_barlow_2 = st.text_input('Define id of Barlow', value="3x", key='bar_2')
        select_barlow_2 = False
        # if st.checkbox(f'Add {name_barlow_2} Barlow'):
        #     select_barlow_2 = True
        #     st.markdown("Barlow Selected = _True_")
        #     with st_stdout("code"), st_stderr("code"):
        #         ota.add_optic(barlow_lens(barlow=factor_2), name_barlow_2, select=select_barlow_2)

    with col8:
        st.markdown("**Barlow 3**")
        factor_3 = st.number_input('Barlow Factor', min_value=1.0, value=5.0, step=1.0, format='%f', key='bar_3')
        name_barlow_3 = st.text_input('Define id of Barlow', value="5x", key='bar_3')
        select_barlow_3 = False
        # if st.checkbox(f'Add {name_barlow_3} Barlow'):
        #     select_barlow_3 = True
        #     st.markdown("Barlow Selected = _True_")
        #     with st_stdout("code"), st_stderr("code"):
        #         ota.add_optic(barlow_lens(barlow=factor_3), name_barlow_3, select=select_barlow_3)

    barlow = st.radio('Choose the Barlow', [f'{name_barlow_1} Barlow', f'{name_barlow_2} Barlow', f'{name_barlow_3} Barlow'])
    if barlow == f'{name_barlow_1} Barlow':
        select_barlow_1 = True
        st.markdown("Barlow Selected = _True_")
        with st_stdout("code"), st_stderr("code"):
            ota.add_optic(barlow_lens(barlow=factor_1), name_barlow_1, select=select_barlow_1)  
    elif barlow == f'{name_barlow_2} Barlow':
        select_barlow_2 = True
        st.markdown("Barlow Selected = _True_")
        with st_stdout("code"), st_stderr("code"):
            ota.add_optic(barlow_lens(barlow=factor_2), name_barlow_2, select=select_barlow_2)
    elif barlow == f'{name_barlow_3} Barlow':
        select_barlow_3 = True
        st.markdown("Barlow Selected = _True_")
        with st_stdout("code"), st_stderr("code"):
            ota.add_optic(barlow_lens(barlow=factor_3), name_barlow_3, select=select_barlow_3)          
with st.expander("Reducers", expanded = False):
    col9, col10, col11 = st.columns([1,1,1])
    with col9:
        st.markdown("**Reducer 1**")
        P_red_1 = st.number_input('Reducer Power', min_value=0.0, max_value=1.0, value=0.5, step=0.1, format='%f', key='red_1')
        name_red_1 = st.text_input('Define id of Reducer', value="0.5x", key='red_1')
        select_red_1 = False
        # if st.checkbox(f'Add {name_red_1} Reducer'):
        #     select_red_1 = True 
        #     st.markdown("Reducer Selected = _True_")
        #     with st_stdout("code"), st_stderr("code"):
        #         ota.add_optic(focal_reducer(P_reducer=P_red_1), name_red_1, select=select_red_1)

    with col10:
        st.markdown("**Reducer 2**")
        P_red_2 = st.number_input('Reducer Power', min_value=0.0, max_value=1.0, value=0.75, step=0.1, format='%f', key='red_2')
        name_red_2 = st.text_input('Define id of Reducer', value="0.75x", key='red_2')
        select_red_2 = False
        # if st.checkbox(f'Add {name_red_2} Reducer'):
        #     select_red_2 = True 
        #     st.markdown("Reducer Selected = _True_")
        #     with st_stdout("code"), st_stderr("code"):
        #         ota.add_optic(focal_reducer(P_reducer=P_red_2), name_red_2, select=select_red_2)

    with col11:
        st.markdown("**Reducer 3**")
        P_red_3 = st.number_input('Reducer Power', min_value=0.0, max_value=1.0, value=0.8, step=0.1, format='%f', key='red_3')
        name_red_3 = st.text_input('Define id of Reducer', value="0.8x", key='red_3')
        select_red_3 = False
        # if st.checkbox(f'Add {name_red_3} Reducer'):
        #     select_red_3 = True 
        #     st.markdown("Reducer Selected = _True_")
        #     with st_stdout("code"), st_stderr("code"):
        #         ota.add_optic(focal_reducer(P_reducer=P_red_3), name_red_3, select=select_red_3)
        
    reducer = st.radio('Choose the Reducer', [f'{name_red_1} Reducer', f'{name_red_2} Reducer', f'{name_red_3} Reducer'])
    if reducer == f'Add {name_red_1} Reducer':
        select_red_1 = True 
        st.markdown("Reducer Selected = _True_")
        with st_stdout("code"), st_stderr("code"):
            ota.add_optic(focal_reducer(P_reducer=P_red_1), name_red_1, select=select_red_1)
    elif reducer == f'Add {name_red_2} Reducer':
        select_red_2 = True 
        st.markdown("Reducer Selected = _True_")
        with st_stdout("code"), st_stderr("code"):
            ota.add_optic(focal_reducer(P_reducer=P_red_2), name_red_2, select=select_red_2)
    elif reducer == f'Add {name_red_3} Reducer':
        select_red_3 = True 
        st.markdown("Reducer Selected = _True_")
        with st_stdout("code"), st_stderr("code"):
            ota.add_optic(focal_reducer(P_reducer=P_red_3), name_red_3, select=select_red_3)
# if select_barlow_1 == select_red_1 == True:
#     st.write("Effective power of additional optic is:", P_red_1*factor_1, 'x')
# elif select_barlow_2 == select_red_2 == True:
#     st.write("Effective power of additional optic is:", P_red_2*factor_2, 'x')
# elif select_barlow_3 == select_red_3 == True:
#     st.write("Effective power of additional optic is:", P_red_3*factor_3, 'x')


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

