import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd


# ---- Page Configuration ---- #
st.set_page_config(page_title='Interactive Dashboard', layout='wide')


# ---- Page Header ---- #
# Column Configuration
column0, column1 = st.columns([3, 2])

# Left Column
with column0:
    st.title('Marcos Vinícius Theodoro Pinheiro da Silva')
    st.subheader('Eletronics and Hardware Coordinator - UFRJ Nautilus')
    st.subheader('Control and Automation Engeneering - UFRJ')
    st.subheader('Industrial Automation Technician - CEFET/RJ')
    st.caption('Since 2019, studying and developing projects related to robotics, control and automation.')

# Right Column
with column1:
    st.image('Data.gif')

# Section Break
st.markdown('***')
