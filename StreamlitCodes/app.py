import streamlit as st
import pandas as pd
import numpy as np
import time
import os 
from google.cloud import bigquery
from streamlit_option_menu import option_menu
import altair as alt
import datetime
from PIL import image

def bqtoapp(query = "SELECT * FROM idsdb.idsdb_table"):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'delta-lore-369612-167298c7b11b.json'
    client = bigquery.Client()
    table_id = "delta-lore-369612.idsdb.idsdb_table"
    QUERY = (query)
    query_job = client.query(QUERY)

    rows = query_job.result()
    row_list = []
    for row in rows:
        value = [row[0],row[1],row[2],row[3],row[4]]
        row_list.append(value)
    
    df = pd.DataFrame(row_list,columns=['flight_date','flight_status','depAirport','arrAirport','airlineName'])
    return df

df = bqtoapp()

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Airport Analysis","Airline Analysis"],
        icons=["airplane-fill","airplane-engines-fill"]
    )
if selected == "Airport Analysis":
    st.title(selected)
    depAirportOption = st.selectbox(
        'Departure Airport',
        pd.unique(df["depAirport"].str.strip())
    )
if selected == "Airline Analysis":
    st.title(selected)
    currencyOption = st.selectbox(
        'Airlines',
        ('DHL Air','Pionair Australia','FedEx','Air Canada','Iberia','Finnair','Jetstar','Eurowings','Air Arabia','Avianca Cargo','Universal Air','Private owner','Tibet Airlines','Xiamen Airlines','Sichuan Airlines','American Airlines','China Express Air','Malaysia Airlines','Philippine Airlines','China Southern Airlines','VietJet Air')
    )
