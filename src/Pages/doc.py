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
        
    col1, col2, col3 = st.columns([1,1,1])
    tel_type = ('Refractor (Diotropics)', 'Reflector (Catatropics)', 'Catadiotropics')
    dio_type = ('Galiliean', 'Achromatic', 'Apochromatic', 'Superachromat')
    cata_type = ('Gregorian', 'Newtonian', 'Nasmyth', 'Ritchey–Chrétien', 'Three-mirror Anastigmat')
    catadio_type = ('Schmidt-Cassegrain', 'Maksutov-Cassegrain', 'Corrected Dall-Krikham')
    with col1: #shows diagram of telescope
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
    
    with col2:
        st.subheader("Eyepiece Diagrams")
    with col3:
        st.subheader("Mount Diagrams")
