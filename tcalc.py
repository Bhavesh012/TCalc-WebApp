import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

from TCalc.tcalc import telescope, eyepiece, barlow_lens, focal_reducer

st.title('TCalc: Telescope-Calculator')
st.write('TCalc is built on the motive to spread awareness about telescopes and how to optimally use them in order to save time, money and sanity! Around 70% of amateur or rising astronomers and telescope owners waste 65% of their savings on buying the wrong or incompatible stuff for their telescope. 90% of them deals with high-level of frustration when trying their eyepieces or barlows.')