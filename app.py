import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd


# ---- Page Configuration ---- #
st.set_page_config(page_title='Graduation Dashboard', layout='wide')


# ---- Page Header ---- #
# Column Configuration
column0, column1 = st.columns([3, 2])

# Left Column
with column0:
    st.title('Marcos Vinícius Theodoro Pinheiro da Silva')
    st.subheader('Electronics and Hardware Coordinator - UFRJ Nautilus')
    st.subheader('Control and Automation Engeneering - UFRJ')
    st.subheader('Industrial Automation Technician - CEFET/RJ')
    st.caption('Since 2019, studying and developing projects related to robotics, control and automation.')

# Right Column
with column1:
    st.image('network.gif')


# ---- Section Break ---- #
st.markdown('***')


# ---- Column Configuration ---- #
column2, column3 = st.columns([1, 1])


# ---- High School History ---- #
# History DataFrame Import
history1 = pd.read_json('highHistory.json', orient ='records')

# History DataFrame Format
history1['Year'] = history1['Year'].astype(str)

# History Insert - Grade x Credits
history1.insert(6, 'Accum. Grade', history1['Grade'] * history1['Credits'])

# Left Column
with column2:
    st.markdown('<h3 style="text-align: center">Technical High School History</h3><br>', unsafe_allow_html=True)
    st.dataframe(data=history1.iloc[:, 0:6], use_container_width=True, height=1578)


# ---- Graduation History ---- #
# History DataFrame Import
history0 = pd.read_json('gradHistory.json', orient ='records')

# History DataFrame Format
history0['Year'] = history0['Year'].astype(str)

# History Insert - Grade x Credits
history0.insert(8, 'Accum. Grade', history0['Grade'] * history0['Credits'])

# Right Column
with column3:
    st.markdown('<h3 style="text-align: center">Graduation History</h3><br>', unsafe_allow_html=True)
    st.dataframe(data=history0.iloc[:, 0:8], use_container_width=True, height=458)


# ---- Section Break ---- #
st.markdown('***')


# ---- Column Configuration ---- #
column4, column5 = st.columns([1, 1])


# ---- High School Performance Coefficient ---- #
# Coefficient - 1st Year
Y1 = round(history1.loc[history1['Year'] == "2019"].iloc[:, 6].sum() / history1.loc[history1['Year'] == "2019"].iloc[:, 3].sum(), 1)

# Coefficient - 2nd Year
Y2 = round(history1.loc[history1['Year'] == "2020"].iloc[:, 6].sum() / history1.loc[history1['Year'] == "2020"].iloc[:, 3].sum(), 1)

# Coefficient - 3rd Year
Y3 = round(history1.loc[history1['Year'] == "2021"].iloc[:, 6].sum() / history1.loc[history1['Year'] == "2021"].iloc[:, 3].sum(), 1)

# Coefficient DataSet
coef1 = [[2019, Y1],
        [2020, Y2],
        [2021, Y3]]

# Coefficient DataFrame
coefficient1 = pd.DataFrame(coef1, columns=['Year', 'Performance Coefficient'])

# Coefficient Histplot
sb.set_style('whitegrid')
plt.figure(figsize=(10, 5))
plt1 = sb.barplot(x='Year', y='Performance Coefficient', data=coefficient1, palette='mako')
plt1.bar_label(plt1.containers[0])
plt1.set(yticklabels=[])
plt1.set_ylabel(None)
plt1.set_xlabel(None)

# Left Column
with column4:
    st.markdown('<h3 style="text-align: center">Technical High School Performance Coefficient</h3><br>', unsafe_allow_html=True)
    st.pyplot(fig=plt1.figure)


#  ---- Graduation Performance Coefficient ---- #
# Coefficient - 1st Period
P1 = round(history0.loc[history0['Period'] == 1].iloc[:, 8].sum() / history0.loc[history0['Period'] == 1].iloc[:, 5].sum(), 1)

# Coefficient - 2nd Period
P2 = round(history0.loc[history0['Period'] <= 2].iloc[:, 8].sum() / history0.loc[history0['Period'] <= 2].iloc[:, 5].sum(), 1)

# Coefficient DataSet
coef0 = [[2022.1, P1],
       [2022.2, P2]]

# Coefficient DataFrame
coefficient0 = pd.DataFrame(coef0, columns=['Period', 'Performance Coefficient'])

# Coefficient Histplot
sb.set_style('whitegrid')
plt.figure(figsize=(10, 5))
plt0 = sb.barplot(x='Period', y='Performance Coefficient', data=coefficient0, palette='mako')
plt0.bar_label(plt0.containers[0])
plt0.set(yticklabels=[])
plt0.set_ylabel(None)
plt0.set_xlabel(None)

# Right Column
with column5:
    st.markdown('<h3 style="text-align: center">Graduation Performance Coefficient</h3><br>', unsafe_allow_html=True)
    st.pyplot(fig=plt0.figure)