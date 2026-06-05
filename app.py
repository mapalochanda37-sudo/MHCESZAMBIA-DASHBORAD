
import streamlit as st
import pandas as pd

# --- SIDEBAR ---
st.sidebar.title("MHC Control Panel")
st.sidebar.divider()

name = st.sidebar.text_input("Engineer Name")
site = st.sidebar.selectbox("Select Site", ["Kitwe Plant", "Ndola Plant", "Mufulira Plant"])

if st.sidebar.button("Login"):
    if name == "":
        st.sidebar.warning(" Enter your name first.")
    else:
        st.sidebar.success(f" Welcome to the {site} ,  Enginner {name}!")

# --- MAIN PAGE ---
st.title("MHC Engineering Solutions Zambia")
st.subheader(f"Site: {site}")
st.divider()

# Voltage Checker
st.header("Voltage Checker")
voltage = st.number_input("Enter Voltage (V)", min_value=0.0)

if st.button("Check Voltage"):
    if voltage == 0:
        st.write("Enter a voltage value to get a result.")
    elif voltage < 180:
        st.success(" Voltage is safe!")
    elif 180 <= voltage < 240:
        st.warning(" Voltage is within the normal range, Monitor closely.")
    elif 240 <= voltage < 300:
        st.warning('Voltage levels are getting high, Take Precautionary Measures!')
    else:
        st.error('Voltage is Dangerously High! Shut Down Immediately!')
st.divider()

# Monthly Voltage Chart
st.header("Monthly Voltage Readings")
data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Voltage (V)": [220, 170, 300, 280, 210, 228]
})
st.line_chart(data.set_index("Month"))

st.divider()

# Equipment Temperature Chart
st.header("Equipment Temperature Report")
st.subheader(f"Showing data for: {site}")

if site == "Kitwe Plant":
    data2 = pd.DataFrame({
        "Equipment": ["Generator", "Pump", "Motor"],
        "Temperature (C)": [75, 60, 85]
    })
elif site == "Ndola Plant":
    data2 = pd.DataFrame({
        "Equipment": ["Generator", "Pump", "Motor"],
        "Temperature (C)": [90, 55, 70]
    })
else:
    data2 = pd.DataFrame({
        "Equipment": ["Generator", "Pump", "Motor"],
        "Temperature (C)": [65, 80, 95]
    })

st.bar_chart(data2.set_index("Equipment"))

st.divider()
st.header('Voltage Log')
st.subheader('Recent readings by engineers')
log=pd.DataFrame({
    'Engineer' : ['Mwamba','Chanda', 'Mapalo' , 'Hope', 'Chomba'],
    'Site' : ['Kitwe Plant' , 'Lusaka Plant' , 'Mufulira Plant', 'Lusaka Plant', 'Ndola Plant'],
    'Voltage (V)': [180,200,300,100,990],
    'Status' : ['Safe' , 'Normal' ,'Dangerous','Safe','Dangerous']
})
st.dataframe(log)