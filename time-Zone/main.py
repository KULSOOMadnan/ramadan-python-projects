import streamlit as st
from datetime import datetime, time
from zoneinfo import ZoneInfo


TIME_ZONES = [
    'UTC',
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Australia/Sydney",
    "Africa/Nairobi",
    "Asia/Shanghai",
    "Asia/Tokyo",
    "America/Los_Angeles",
    "America/Chicago",
    'Asia/Dubai',
    'Asia/Kolkata',
    'Asia/Hong_Kong',
    'Asia/Seoul',
    'Asia/Bangkok',
    'Asia/Jakarta',
    'Asia/Manila',
]


st.title('Time Zone Converter')

selected_time_zone = st.multiselect('Select Timezones', TIME_ZONES , default=['UTC' , 'Asia/Karachi'])

st.write('---')

st.subheader('Selected Timezones')


for tz in selected_time_zone:
    
    current_time = datetime.now(ZoneInfo(tz))
    formatted_time = current_time.strftime('%Y-%m-%d %I %H:%M:%S %p')
    st.write(f'**{tz}** : {formatted_time}')
    st.write('---')
    
    
st.subheader('Convert Time Between Timezones')

# Get the current time as a time object
current_time_input = st.time_input("Current Time", value=datetime.now().time())

# Convert the time object to a datetime object for further processing
current_time = datetime.combine(datetime.today(), current_time_input)

# Provide a list of time zones for selection
from_tz = st.selectbox('From Timezone', TIME_ZONES , index=0)

to_tz = st.selectbox("To Timezone" , TIME_ZONES , index=1)

st.write('---')

st.subheader('Time Difference')

if st.button('convert Time'):
    dt = datetime.combine(datetime.today(), current_time_input , tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime('%Y-%m-%d %I %H:%M:%S %p')
    st.write(f'**{from_tz}** : {dt}')
    st.write(f'**{to_tz}** : {converted_time}')



