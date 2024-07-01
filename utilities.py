import pandas as pd
import numpy as np
import folium
import plotly.express as px
import streamlit as st
from streamlit_folium import folium_static
from datetime import datetime
from PIL import Image
from haversine import haversine
import plotly.graph_objects as go


def clean_code(df1):
    """This function clean the code.

    Types of cleaning:

    1. Convert object to int
    2. convert text to float
    3. Convert text to datetime
    4. Remove all NaN
    5. Remove blanks from texts
    6. Split text and number and transform the data to int

    """

    # Converting column Ages and multiple_deliveries from object to int
    linhas_selecionadas = df1['Delivery_person_Age'] != 'NaN '
    df1 = df1.loc[linhas_selecionadas, :].copy()
    df1['Delivery_person_Age'] = df1['Delivery_person_Age'].astype(int)

    linhas_selecionadas = df1['multiple_deliveries'] != 'NaN '
    df1 = df1.loc[linhas_selecionadas, :].copy()
    df1['multiple_deliveries'] = df1['multiple_deliveries'].astype(int)

    # Converting column Ratings from text to float
    df1['Delivery_person_Ratings'] = (df1['Delivery_person_Ratings']
                                      .astype(float))

    # Converting column Order_Date from text to datetime
    df1['Order_Date'] = pd.to_datetime(df1['Order_Date'], format='%d-%m-%Y')

    # Removing NaN from Road_traffic_density, City and Festival
    linhas_selecionadas = df1['Road_traffic_density'] != 'NaN '
    df1 = df1.loc[linhas_selecionadas, :].copy()

    linhas_selecionadas = df1['City'] != 'NaN '
    df1 = df1.loc[linhas_selecionadas, :].copy()

    linhas_selecionadas = df1['Festival'] != 'NaN '
    df1 = df1.loc[linhas_selecionadas, :].copy()

    # Removing blanks from strings
    df1.loc[:, 'ID'] = df1.loc[:, 'ID'].str.strip()
    df1.loc[:, 'Delivery_person_ID'] = (df1.loc[:, 'Delivery_person_ID']
                                        .str.strip())
    df1.loc[:, 'Weatherconditions'] = (df1.loc[:, 'Weatherconditions']
                                       .str.strip())
    df1.loc[:, 'Road_traffic_density'] = (df1.loc[:, 'Road_traffic_density']
                                          .str.strip())
    df1.loc[:, 'Type_of_order'] = df1.loc[:, 'Type_of_order'].str.strip()
    df1.loc[:, 'Type_of_vehicle'] = df1.loc[:, 'Type_of_vehicle'].str.strip()
    df1.loc[:, 'Festival'] = df1.loc[:, 'Festival'].str.strip()
    df1.loc[:, 'City'] = df1.loc[:, 'City'].str.strip()

    # Removing texts from Time_taken(min) column and turning into int
    df1['Time_taken(min)'] = (df1['Time_taken(min)']
                              .apply(lambda x: x.split('(min)')[1]))
    df1['Time_taken(min)'] = df1['Time_taken(min)'].astype(int)

    # Removing texts from Weatherconditions column
    df1['Weatherconditions'] = (df1['Weatherconditions']
                                .apply(lambda x: x.split('conditions ')[1]))

    return df1


def side_bar_company_config(df1):

    st.header('Marketplace - Company Dashboard')

    # image_path = 'projetos/logo.png'
    image = Image.open('logo.png')
    st.sidebar.image(image, width=120)

    st.sidebar.markdown('# Curry Company')
    st.sidebar.markdown('#### Fastest delivery in town')
    st.sidebar.markdown("""---""")

    date_slider = st.sidebar.slider(
        'Choose a date',
        value=datetime(2022, 4, 10),
        min_value=datetime(2022, 2, 11),
        max_value=datetime(2022, 4, 6),
        format='DD-MM-YYYY')

    st.sidebar.markdown("""---""")

    traffic_options = st.sidebar.multiselect(
        'Traffic conditions',
        ['Low', 'Medium', 'High', 'Jam'],
        default=['Low', 'Medium', 'High', 'Jam'])

    st.sidebar.markdown("""---""")
    st.sidebar.markdown('#### Powered by Felipe Valory')

    # Filtro de data
    linhas_selecionadas = df1['Order_Date'] <= date_slider
    df1 = df1.loc[linhas_selecionadas, :]

    # Filtro de trânsito
    linhas_selecionadas = df1['Road_traffic_density'].isin(traffic_options)
    df1 = df1.loc[linhas_selecionadas, :]

    return df1


def side_bar_deliverer_config(df1):
    st.header('Marketplace - Deliverer Dashboard')

    # image_path = 'projetos/logo.png'
    image = Image.open('logo.png')
    st.sidebar.image(image, width=120)

    st.sidebar.markdown('# Curry Company')
    st.sidebar.markdown('#### Fastest delivery in town')
    st.sidebar.markdown("""---""")

    date_slider = st.sidebar.slider(
        'Choose a date',
        value=datetime(2022, 4, 10),
        min_value=datetime(2022, 2, 11),
        max_value=datetime(2022, 4, 6),
        format='DD-MM-YYYY')

    st.sidebar.markdown("""---""")

    traffic_options = st.sidebar.multiselect(
        'Traffic conditions',
        ['Low', 'Medium', 'High', 'Jam'],
        default=['Low', 'Medium', 'High', 'Jam'])

    weatherconditions_options = st.sidebar.multiselect(
        'Weatherconditions',
        ['Cloudy', 'Fog', 'Sandstorms', 'Stormy', 'Sunny', 'Windy'],
        default=['Cloudy', 'Fog', 'Sandstorms', 'Stormy', 'Sunny', 'Windy'])

    st.sidebar.markdown("""---""")
    st.sidebar.markdown('#### Powered by Felipe Valory')

    # Filtro de data
    linhas_selecionadas = df1['Order_Date'] <= date_slider
    df1 = df1.loc[linhas_selecionadas, :]

    # Filtro de trânsito
    linhas_selecionadas = df1['Road_traffic_density'].isin(traffic_options)
    df1 = df1.loc[linhas_selecionadas, :]

    # Filtro de condição climatica
    linhas_selecionadas = (df1['Weatherconditions']
                           .isin(weatherconditions_options))
    df1 = df1.loc[linhas_selecionadas, :]

    return df1


def side_bar_restaurants_config(df1):
    st.header('Marketplace - Restaurants Dashboard')

    # image_path = 'projetos/logo.png'
    image = Image.open('logo.png')
    st.sidebar.image(image, width=120)

    st.sidebar.markdown('# Curry Company')
    st.sidebar.markdown('#### Fastest delivery in town')
    st.sidebar.markdown("""---""")

    date_slider = st.sidebar.slider(
        'Choose a date',
        value=datetime(2022, 4, 10),
        min_value=datetime(2022, 2, 11),
        max_value=datetime(2022, 4, 6),
        format='DD-MM-YYYY')

    st.sidebar.markdown("""---""")

    traffic_options = st.sidebar.multiselect(
        'Traffic conditions',
        ['Low', 'Medium', 'High', 'Jam'],
        default=['Low', 'Medium', 'High', 'Jam'])

    weatherconditions_options = st.sidebar.multiselect(
        'Weatherconditions',
        ['Cloudy', 'Fog', 'Sandstorms', 'Stormy', 'Sunny', 'Windy'],
        default=['Cloudy', 'Fog', 'Sandstorms', 'Stormy', 'Sunny', 'Windy'])

    st.sidebar.markdown("""---""")
    st.sidebar.markdown('#### Powered by Felipe Valory')

    # Filtro de data
    linhas_selecionadas = df1['Order_Date'] <= date_slider
    df1 = df1.loc[linhas_selecionadas, :]

    # Filtro de trânsito
    linhas_selecionadas = df1['Road_traffic_density'].isin(traffic_options)
    df1 = df1.loc[linhas_selecionadas, :]

    # Filtro de condição climatica
    linhas_selecionadas = (df1['Weatherconditions']
                           .isin(weatherconditions_options))
    df1 = df1.loc[linhas_selecionadas, :]

    return df1


def order_by_day(df1):
    df_aux = (df1[['ID', 'Order_Date']].groupby('Order_Date').count()
              .reset_index())
    df_aux.columns = ['Days', 'Orders']
    fig = px.bar(df_aux, x='Days', y='Orders')

    return fig


def traffic_order_share(df1):
    df_aux = (df1[['ID', 'Road_traffic_density']]
              .groupby('Road_traffic_density').count().reset_index())

    df_aux['entregas_perc'] = (round((df_aux['ID'] / df_aux['ID']
                                      .sum())*100, 2))

    fig = px.pie(df_aux, values='entregas_perc', names='Road_traffic_density')

    return fig


def traffic_order_city(df1):
    df_aux = (df1[['ID', 'City', 'Road_traffic_density']]
              .groupby(['City', 'Road_traffic_density'])
              .count().reset_index())

    fig = (px.scatter(df_aux, x='City', y='Road_traffic_density',
                      size='ID', color='City'))

    return fig


def order_by_week(df1):
    # Create a week column
    df1['week'] = df1['Order_Date'].dt.strftime('%U')
    df_aux = df1[['ID', 'week']].groupby('week').count().reset_index()
    df_aux.columns = ['Week', 'Orders']

    fig = px.line(df_aux, x='Week', y='Orders')

    return fig


def order_by_deliverer_week(df1):
    week_orders = df1[['ID', 'week']].groupby('week').count().reset_index()
    week_deliverer = (df1[['Delivery_person_ID', 'week']].groupby('week')
                      .nunique().reset_index())
    df_aux = pd.merge(week_orders, week_deliverer, how='inner')
    df_aux['Orders_by_deliverer'] = (round(df_aux['ID'] /
                                           df_aux['Delivery_person_ID'], 2))

    fig = px.line(df_aux, x='week', y='Orders_by_deliverer')

    return fig


def map_maker(df1):
    df_aux = (df1[['City', 'Delivery_location_latitude',
                   'Delivery_location_longitude', 'Road_traffic_density']]
              .groupby(['City', 'Road_traffic_density'])
              .median().reset_index())

    map_ = folium.Map()

    for index, location_info in df_aux.iterrows():
        (folium.Marker([location_info['Delivery_location_latitude'],
                        location_info['Delivery_location_longitude']],
         popup=location_info[['City', 'Road_traffic_density']]).add_to(map_))

    folium_static(map_, width=700, height=400)


def ratings_deliverer(df1):
    df1 = df1[['Delivery_person_Ratings', 'Delivery_person_ID']]
    df1.columns = ['Average_ratings', 'Deliverer']
    df1 = (round(df1[['Deliverer', 'Average_ratings']]
                 .groupby('Deliverer').mean()
                 .reset_index(), 2))
    return df1


def ratings_traffic(df1):
    df1 = round(df1[['Delivery_person_Ratings', 'Road_traffic_density']]
                .groupby('Road_traffic_density')
                .agg(['mean', 'std']), 2)
    df1.columns = ['ratings_mean', 'ratings_std']
    df1.reset_index()

    return df1


def ratings_weather(df1):
    df1 = (round(df1[['Delivery_person_Ratings', 'Weatherconditions']]
                 .groupby('Weatherconditions')
                 .agg(['mean', 'std']), 2))
    df1.columns = ['ratings_mean', 'ratings_std']
    df1.reset_index()

    return df1


def fastest_slowest_deliverer(df1, top_asc):
    df2 = df1[['Delivery_person_ID', 'Time_taken(min)', 'City']]
    df2.columns = ['Deliverer', 'Time_taken(min)', 'City']
    df2 = (round(df2[['Deliverer', 'Time_taken(min)', 'City']]
                 .groupby(['City', 'Deliverer'])
                 .mean().sort_values(['City', 'Time_taken(min)'],
                                     ascending=top_asc).reset_index(), 2))

    df3 = df2.loc[df2['City'] == 'Metropolitian', :].head(10)
    df4 = df2.loc[df2['City'] == 'Semi-Urban', :].head(10)
    df5 = df2.loc[df2['City'] == 'Urban', :].head(10)
    df6 = pd.concat([df3, df4, df5]).reset_index(drop=True)

    return df6


def mean_distance_from_restaurants(df1):
    cols = ['Restaurant_latitude', 'Restaurant_longitude',
            'Delivery_location_latitude',
            'Delivery_location_longitude']
    df1['distance'] = (df1.loc[:, cols]
                       .apply(lambda x: haversine((
                                        x['Restaurant_latitude'],
                                        x['Restaurant_longitude']),
                                       (x['Delivery_location_latitude'],
                                        x['Delivery_location_longitude'])),
                              axis=1))
    mean_distance = round(df1['distance'].mean(), 2)

    return mean_distance


def avg_std_delivery_time(df1, festival, op):

    """
        This function calculate the avg and std delivery time.

        Input:
            - df: Dataframe
            - festival: Yes or No (deliveries are doing through
                                    the festival or not)
            - op: Operation type
                    'avg_time': calculate the avg delivery time
                    'std_time': calculate the standard deviation delivery time
    """

    df_aux = (round(df1[['Time_taken(min)', 'Festival']]
                    .groupby('Festival').agg(['mean', 'std']), 2))
    df_aux.columns = ['avg_time', 'std_time']
    df_aux = df_aux.reset_index()
    df_aux = round(df_aux.loc[df_aux['Festival'] == festival, op], 2)

    return df_aux


def avg_distance_graphic(df1):
    cols = ['Delivery_location_latitude', 'Delivery_location_longitude',
            'Restaurant_latitude', 'Restaurant_longitude']
    df1['distance'] = (df1.loc[:, cols]
                       .apply(lambda x: haversine(
                                    (x['Restaurant_latitude'],
                                     x['Restaurant_longitude']),
                                    (x['Delivery_location_latitude'],
                                     x['Delivery_location_longitude'])),
                              axis=1))
    avg_distance = (df1.loc[:, ['City', 'distance']].groupby('City').mean()
                    .reset_index())

    fig = (go.Figure(data=[go.Pie(labels=avg_distance['City'],
                                  values=avg_distance['distance'],
                                  pull=[0, 0.1, 0])]))
    return fig


def delivery_time_by_city_graphic(df1):
    df_aux = (df1.loc[:, ['Time_taken(min)', 'City']].groupby(['City'])
              .agg({'Time_taken(min)': ['mean', 'std']}))
    df_aux.columns = ['avg_time', 'std_time']
    df_aux = df_aux.reset_index()

    fig = go.Figure()

    (fig.add_trace(go.Bar(name='Control', x=df_aux['City'],
                          y=df_aux['avg_time'],
                          error_y=dict(type='data',
                          array=df_aux['std_time']))))
    fig.update_layout(barmode='group')

    return fig


def delivery_time_by_city_by_order_graphic(df1):
    df_aux = (round(df1[['Time_taken(min)', 'City', 'Type_of_order']]
                    .groupby(['City', 'Type_of_order'])
                    .agg(['mean', 'std']), 2))
    df_aux.columns = ['avg_time', 'std_time']
    df_aux = df_aux.reset_index()

    fig = (px.sunburst(df_aux, path=['City', 'Type_of_order'],
                       values='avg_time', color='std_time',
                       color_continuous_scale='RdBu',
                       color_continuous_midpoint=np.average(
                       df_aux['std_time'])))
    return fig


def avg_time_delivery_by_city_by_traffic(df1):
    df_aux = (round(df1[['Time_taken(min)', 'City', 'Road_traffic_density']]
                    .groupby(['City', 'Road_traffic_density'])
                    .agg(['mean', 'std']), 2))

    df_aux.columns = ['avg_time', 'std_time']

    df_aux = df_aux.reset_index()

    return df_aux
