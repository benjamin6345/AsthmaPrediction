import streamlit as st
from RealTime import get_now_weather
from ThreeDaysReport import get_three_days_temp

get_three_days_temp()
get_now_weather()
st.markdown('Hi')
