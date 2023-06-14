import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd


# ---- Page Configuration ---- #
st.set_page_config(page_title='Academic Dashboard', layout='wide')


# ---- Page Header ---- #
# Column Configuration
column0, column1 = st.columns([2.5, 2])

# Left Column
with column0:
    st.title('Marcos Vinícius Theodoro')
    st.subheader('Control and Automation Engineering - UFRJ')
    st.subheader('Industrial Automation Technician - CEFET/RJ')
    st.caption('Since 2019, studying and developing projects related to robotics, control and automation.')


st.markdown('***')


# ---- Column Configuration ---- #
column2, column3 = st.columns([1, 1])


# ---- High School History ---- #
# History DataFrame Import
history0 = pd.read_json('highHistory.json', orient ='records')

# History DataFrame Format
history0['Year'] = history0['Year'].astype(str)

# History Insert - Grade x Credits
history0.insert(6, 'Accum. Grade', history0['Grade'] * history0['Credits'])

# Left Column
with column2:
    st.markdown('<h3 style="text-align: center">Technical High School History</h3><br>', unsafe_allow_html=True)
    st.dataframe(data=history0.iloc[:, 0:5], use_container_width=True, height=1578)


# ---- Graduation History ---- #
# History DataFrame Import
history1 = pd.read_json('gradHistory.json', orient ='records')

# History DataFrame Format
history1['Year'] = history1['Year'].astype(str)

# History Insert - Grade x Credits
history1.insert(8, 'Accum. Grade', history1['Grade'] * history1['Credits'])

# Right Column
with column3:
    st.markdown('<h3 style="text-align: center">Graduation History</h3><br>', unsafe_allow_html=True)
    st.dataframe(data=history1.iloc[:, 0:7], use_container_width=True, height=458)


# ---- Performance Coefficient ---- #
# Coefficient - 1st Year
Y1 = round(history0.loc[history0['Year'] == "2019"].iloc[:, 6].sum() / history0.loc[history0['Year'] == "2019"].iloc[:, 3].sum(), 1)

# Coefficient - 2nd Year
Y2 = round(history0.loc[history0['Year'] == "2020"].iloc[:, 6].sum() / history0.loc[history0['Year'] == "2020"].iloc[:, 3].sum(), 1)

# Coefficient - 3rd Year
Y3 = round(history0.loc[history0['Year'] == "2021"].iloc[:, 6].sum() / history0.loc[history0['Year'] == "2021"].iloc[:, 3].sum(), 1)

# Coefficient - 1st Period
P1 = round(history1.loc[history1['Period'] == 1].iloc[:, 8].sum() / history1.loc[history1['Period'] == 1].iloc[:, 5].sum(), 1)

# Coefficient - 2nd Period
P2 = round(history1.loc[history1['Period'] <= 2].iloc[:, 8].sum() / history1.loc[history1['Period'] <= 2].iloc[:, 5].sum(), 1)

# Coefficient DataSet
coef = [['2019', Y1],
        ['2020', Y2],
        ['2021', Y3],
        ['2022.1', P1],
        ['2022.2', P2]]

# Coefficient DataFrame
coefficient = pd.DataFrame(coef, columns=['Period', 'Performance Coefficient'])

# Coefficient Scatterplot
sb.set_style('whitegrid')
plt.figure(figsize=(10, 3.3))
plt0 = sb.stripplot(x='Period', y='Performance Coefficient', data=coefficient, palette='mako')
plt0.set_title('Academic Performance Coefficient')
plt0.set_ylim(7.8, 9.2)
plt0.set_ylabel(None)
plt0.set_xlabel(None)

# Right Column
with column1:
    st.pyplot(fig=plt0.figure)
