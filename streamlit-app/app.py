import streamlit as st


# Import necessary modules after authentication
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