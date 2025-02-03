import streamlit as st
from pathlib import Path
import streamlit as st

st.title('MissedMatch')

st.subheader('Medical Appointment No Shows')

st.write(
"""A person makes a doctor appointment, receives all the instructions and no-show. Who to blame?
If this help you studying or working, please don´t forget to upvote :). Reference to Joni Hoppen and Aquarela Analytics
Greetings!""")

st.write(""""
110.527 medical appointments its 14 associated variables (characteristics). The most important one if the patient show-up or no-show to the appointment. Variable names are self-explanatory, if you have doubts, just let me know!

scholarship variable means this concept = https://en.wikipedia.org/wiki/Bolsa_Fam%C3%ADlia """)

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

intro_markdown = read_markdown_file("report.md")
st.markdown(intro_markdown, unsafe_allow_html=True)