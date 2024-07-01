import pandas as pd
import streamlit as st
from utilities import (clean_code, side_bar_company_config, order_by_day,
                       traffic_order_share, traffic_order_city, order_by_week,
                       order_by_deliverer_week, map_maker)

st.set_page_config(page_title='Company Dashboard', layout='wide')

df = pd.read_csv('../ftc_python/dataset/_train.csv')

df1 = clean_code(df)

df1 = side_bar_company_config(df1)

tab1, tab2, tab3 = st.tabs(['Management', 'Business Strategy', 'Geografic'])

with tab1:
    with st.container():
        # Order_per_day
        st.markdown('## Orders by day')
        fig = order_by_day(df1)
        st.plotly_chart(fig, use_container_width=True)

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('## Traffic Order Share')
            fig = traffic_order_share(df1)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown('## Traffic Order City')
            fig = traffic_order_city(df1)
            st.plotly_chart(fig, use_container_width=True)

with tab2:
    with st.container():
        st.markdown('## Orders by week')
        fig = order_by_week(df1)
        st.plotly_chart(fig, use_container_width=True)

    with st.container():
        st.markdown('## Orders by deliverer per week')
        fig = order_by_deliverer_week(df1)
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.markdown('## City by traffic conditions')
    map_maker(df1)
