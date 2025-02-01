import streamlit as st
from streamlit_auth import authenticate

# Define a username and password for authentication
USERNAME = "ahmed"
PASSWORD = "ahmed"

# Add authentication to your app
if not authenticate(USERNAME, PASSWORD):
    st.error("Authentication failed. Please check your credentials.")
    st.stop()

# Import necessary modules after authentication
import pandas as pd

Home = st.Page(
  page='pages/home.py'
)

Prediction = st.Page(
  page='pages/prediction.py'
)

Analysis = st.Page(
  page='pages/analysis.py'
)

pages = st.navigation(
  [Home, Prediction, Analysis]
)

pages.run()