import streamlit as st
import pandas as pd
import streamlit_option_menu
from streamlit_option_menu import option_menu

Home = st.Page(
  page='home.py'
)

Prediction = st.Page(
  page='prediction.py'
)

Analysis = st.Page(
  page='analysis.py'
)
pages = st.navigation([Home,Prediction,Analysis])

pages.run()
