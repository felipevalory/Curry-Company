import streamlit as st
from PIL import Image

st.set_page_config(page_title='Home')

# image_path = 'projetos/logo.png'
image = Image.open('logo.png')
st.sidebar.image(image, width=120)

st.sidebar.markdown('# Curry Company')
st.sidebar.markdown('#### Fastest delivery in town')
st.sidebar.markdown("""---""")

st.write('# Curry Company Growth Dashboard')

st.write("""
            This dashboard was created to manage important metrics about
            restaurants and deliverers.

        ## How to use it?


        -	### Company vision

            --	Management: Overall metrics

            --	Business Strategy: Weekly statistics

            --	Geografic: Geolocation's insights


        - ### Deliverer vision

            -- Monitoring weekly growth indicators

        - ### Restaurant vision

            -- Weekly restaurant growth indicators
            """)
