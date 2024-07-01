# Libraries
import pandas as pd
import streamlit as st
from utilities import (clean_code, side_bar_restaurants_config,
                       mean_distance_from_restaurants, avg_std_delivery_time,
                       avg_distance_graphic, delivery_time_by_city_graphic,
                       delivery_time_by_city_by_order_graphic,
                       avg_time_delivery_by_city_by_traffic)

st.set_page_config(page_title='Restaurant Dashboard', layout='wide')

df = pd.read_csv('dataset/_train.csv')

df1 = clean_code(df)

df1 = side_bar_restaurants_config(df1)

tab1, tab2, tab3 = st.tabs(['Management Vision', '-', '-'])

with tab1:
    with st.container():
        st.markdown('## Overall Metrics')

        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            deliverer = df1['Delivery_person_ID'].nunique()
            col1.metric('Delivery men', deliverer)

        with col2:
            col2.metric('Avg Distance', mean_distance_from_restaurants(df1))

        with col3:
            col3.metric('Avg time Festival', avg_std_delivery_time(df1, 'Yes',
                                                                   'avg_time'))

        with col4:
            col4.metric('Std Festival', avg_std_delivery_time(df1, 'Yes',
                                                              'std_time'))

        with col5:
            col5.metric('Avg time', avg_std_delivery_time(df1, 'No',
                                                          'avg_time'))

        with col6:
            col6.metric('Std', avg_std_delivery_time(df1, 'No', 'std_time'))

    with st.container():
        st.markdown("""---""")
        st.markdown('### Avg Distance from restaurants to delivery location')

        fig = avg_distance_graphic(df1)
        st.plotly_chart(fig)

    with st.container():
        st.markdown("""---""")
        st.markdown('## Time Metrics')

        col1, col2 = st.columns(2)

        with col1:
            st.markdown('Avg Delivery Time by City')
            fig = delivery_time_by_city_graphic(df1)
            st.plotly_chart(fig)

        with col2:
            st.markdown('Avg Delivery Time by City by Type Order')
            fig = delivery_time_by_city_by_order_graphic(df1)
            st.plotly_chart(fig)

    with st.container():
        st.markdown("""---""")
        st.markdown('##### Avg Delivery Time x City x Traffic Density')
        df_aux = avg_time_delivery_by_city_by_traffic(df1)
        st.dataframe(df_aux)
