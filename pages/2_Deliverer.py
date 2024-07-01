import pandas as pd
import streamlit as st
from utilities import (clean_code, side_bar_deliverer_config,
                       ratings_deliverer, ratings_traffic,
                       ratings_weather, fastest_slowest_deliverer)

st.set_page_config(page_title='Deliverer Dashboard', layout='wide')

df = pd.read_csv('../ftc_python/dataset/_train.csv')

df1 = clean_code(df)

df1 = side_bar_deliverer_config(df1)

tab1, tab2, tab3 = st.tabs(['Management Vision', '-', '-'])

with tab1:
    with st.container():
        st.title('Overall Metrics')

        col1, col2, col3, col4 = st.columns(4, gap='large')
        with col1:
            oldest = df1.loc[:, 'Delivery_person_Age'].max()
            col1.metric('The oldest', oldest)

        with col2:
            youngest = df1.loc[:, 'Delivery_person_Age'].min()
            col2.metric('The youngest', youngest)

        with col3:
            best_vehicle = df1['Vehicle_condition'].max()
            col3.metric('Best vehicle rate', best_vehicle)

        with col4:
            worst_vehicle = df1['Vehicle_condition'].min()
            col4.metric('Worst vehicle rate', worst_vehicle)

    with st.container():
        st.markdown("""---""")
        st.title('Ratings')

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('##### Avg ratings per deliverer')
            df_aux = ratings_deliverer(df1)
            st.dataframe(df_aux)

        with col2:
            st.markdown('##### Avg ratings per traffic conditions')
            df_aux = ratings_traffic(df1)
            st.dataframe(df_aux)

        with col3:
            st.markdown('##### Avg ratings per weatherconditions')
            df_aux = ratings_weather(df1)
            st.dataframe(df_aux)

    with st.container():
        st.markdown("""---""")
        st.title('ETA')
        # Estimated time of arrival

        col1, col2 = st.columns(2)

        with col1:
            st.markdown('##### The fastest deliverer')
            st.dataframe(fastest_slowest_deliverer(df1, True))

        with col2:
            st.markdown('##### The slowest deliverer')
            st.dataframe(fastest_slowest_deliverer(df1, False))
