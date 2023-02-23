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


# ---- Academic History ---- #
# Column Configuration
column2, column3 = st.columns([6, 2])

# History DataSet
hist = [['2022', 1, 1, 'Cálculo I', 'MAC118', 6, 6.4, 'Approved'],
       ['2022', 1, 1, 'Algoritmos e Programação', 'COS110', 5, 10.0, 'Approved'],
       ['2022', 1, 1, 'Lógica Matemática', 'COS230', 5, 9.4, 'Approved'],
       ['2022', 1, 1, 'Química', 'IQG111', 4, 8.0, 'Approved'],
       ['2022', 1, 1, 'Física I', 'FIT112', 4, 5.2, 'Approved'],
       ['2022', 1, 1, 'Introdução à Eng. Controle', 'COE100', 2, 10.0, 'Approved'],
       ['2022', 1, 1, 'Física Experimental I', 'FIS112', 1, 5.0, 'Approved'],
       ['2022', 2, 2, 'Linguagens de Programação', 'EEL670', 5, 10.0, 'Approved'],
       ['2022', 2, 2, 'Circuitos Lógicos', 'EEL280', 5, 7.7, 'Approved'],
       ['2022', 2, 2, 'Economia A', 'EEI312', 4, 10.0, 'Approved'],
       ['2022', 2, 2, 'Sistemas Projetivos', 'EEG110', 4, 8.3, 'Approved'],
       ['2022', 2, 2, 'Física Experimental II', 'FIS121', 1, 7.7, 'Approved']]

# History DataFrame Configuration
history = pd.DataFrame(hist, columns=['Year', 'Semester', 'Period', 'Subject', 'Code', 'Credits', 'Grade', 'Situation'])

# History Insert - Grade x Credits
history.insert(8, 'Accum. Grade', history['Grade'] * history['Credits'])

# Left Column
with column2:
    st.dataframe(data=history, use_container_width=True, height=458)


