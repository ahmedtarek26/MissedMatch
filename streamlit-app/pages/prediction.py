# Import libraries
import random
import streamlit as st
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score,mean_absolute_error,mean_squared_error,f1_score
from sklearn.preprocessing import MinMaxScaler
from collections import Counter
from imblearn.under_sampling import NearMiss
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

#Read Proccessed Data
df = pd.read_csv('/MissedMatch/data/processed/KaggleV2-May-2016-proccessed.csv')

X_input = df.drop(columns=['No-show'])
y = df['No-show']

scaler = MinMaxScaler()
X = scaler.fit_transform(X_input)

# Balance the Data
# Perform NearMiss undersampling to handle imbalanced data
print(f'Test dataset samples per class {Counter(y)}')
 
# Define the NearMiss undersampling object with a sampling strategy of 1 and all available CPU cores
nm = NearMiss(sampling_strategy=1, n_jobs=-1)
 
# Perform NearMiss undersampling on the feature matrix X and target variable y
X, y = nm.fit_resample(X, y)
 
# Print the number of occurrences of each class in the resampled dataset
print('Resampled dataset shape %s' % Counter(y))

# Best Model after testing in the notebook
X_train_rs, X_test_rs, y_train_rs, y_test_rs = train_test_split(X, y, test_size = 0.3, random_state = 4)

rf = RandomForestClassifier( random_state=0 , criterion= 'gini' , max_features='sqrt' , min_samples_split= 2 , n_estimators= 500) 
 # we will use GridSearch
rf.fit(X_train_rs , y_train_rs)




## Prediction part

st.title('Predict the attendance possibility')
st.subheader("Predict if the patient 'll attend the appointement or no")

X_1=5

with st.form(key='best_model'):

    age = st.slider("Add the age", 0, 100, 20)

    sms_recieved = st.selectbox(
        "The patient recieved SMS ? (choose 1 if yes or 0 if no)",
        (1, 0),
    )

    prev_app = st.slider(
        "Number of previous appointments for this patient", 0, 100, 20)

    prev_noshow = st.slider(
        "Number of ignored previous appointments for this patient", 0, 100, 20)

    day_diff = st.slider(
        "Number of days in differences between the appointment and the next scheduled appointment", 0, 200, 20)
    
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        pred = X_test_rs[0]
        pred[1] = age/100
        pred[6] = sms_recieved
        pred[7] = prev_app/100
        pred[8] = prev_noshow/100
        pred[9] = day_diff/200


        X_1 = rf.predict(scaler.fit_transform(pred.reshape(1,-1)))

if X_1 == 1:
    st.subheader("This patient predicted to attend the appointment")
elif X_1 == 0:
    st.subheader("This patient predicted not to attend the appointment")
