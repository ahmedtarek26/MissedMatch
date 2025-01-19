import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Data Analytics and Visualization')

df = pd.read_csv(r'data/raw/KaggleV2-May-2016.csv')
st.subheader('Data before processing')
st.write(df.head())

st.subheader('Some data statistical results')
st.write(df.describe())

# Create a bar chart using st.bar_chart
st.subheader('Gender Distribution')
st.bar_chart(df['Gender'].value_counts())

# Create a bar chart using st.bar_chart
st.subheader('SMS received or no')
st.bar_chart(df['SMS_received'].value_counts())


# Get numerical columns
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns

# Display the histograms in Streamlit
st.title("Histograms of Numerical Features")

for column in numerical_columns:
    fig, ax = plt.subplots()
    ax.hist(df[column], bins=20, alpha=0.5)
    ax.set_title(f"Histogram of {column}")
    st.pyplot(fig)
    plt.clf()  # Clear the current figure

st.subheader('Feature importanc with ELi5')
st.image(r'\streamlit-app\resources\img\eli5.png')

st.subheader('Feature importanc with sklearn')
st.image(r'/streamlit-app/resources/img/sklearn.png')

st.subheader('Feature importanc with Mean decrease in impurity')
st.image(r'/streamlit-app/resources/img/MDI.png')