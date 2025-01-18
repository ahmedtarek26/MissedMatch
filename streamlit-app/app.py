import streamlit as st
import pandas as pd
# import streamlit_option_menu
# from streamlit_option_menu import option_menu

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
  [Home,Prediction,Analysis]
  )

pages.run()
