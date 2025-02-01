# Import libraries
import mlflow
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score,mean_absolute_error,mean_squared_error,f1_score
from sklearn.preprocessing import MinMaxScaler
from collections import Counter
from imblearn.under_sampling import NearMiss
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

#Read Proccessed Data
df = pd.read_csv('/workspaces/MissedMatch/data/processed/KaggleV2-May-2016-proccessed.csv')

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

# Best Model after testing in the notebook (RF)
X_train, X_test , y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 4)

rf = RandomForestClassifier( random_state=0 , criterion= 'gini' , max_features='sqrt' , min_samples_split= 2 , n_estimators= 500) 
 # we will use GridSearch
rf.fit(X_train , y_train)

y_pred_rs = rf.predict(X_test)

rf_acc = accuracy_score(y_test, y_pred_rs)
rf_mae = mean_absolute_error(y_test, y_pred_rs)
rf_mse = mean_squared_error(y_test, y_pred_rs)
rf_f1 = f1_score(y_test, y_pred_rs)

## Second best model SVM

SVC_model = make_pipeline(StandardScaler(),SVC(gamma='auto'))
SVC_model.fit(X_train, y_train)

y_pred_svm = SVC_model.predict(X_test)

svm_acc = accuracy_score(y_test, y_pred_svm)
svm_mae = mean_absolute_error(y_test, y_pred_svm)
svm_mse = mean_squared_error(y_test, y_pred_svm)
svm_f1 = f1_score(y_test, y_pred_svm)
# # mlflow step

# # Define the model hyperparameters
rf_params = {
    "random_state":0 , 
    "criterion":'gini' , 
    "max_features":'sqrt' , 
    "min_samples_split": 2 , 
    "n_estimators": 500
}

svm_params = {
    "gamma": 'auto'
}

# Set our tracking server uri for logging
mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")

# Create a new MLflow Experiment
mlflow.set_experiment("MissedMatch")

# Start an MLflow run

## RF
with mlflow.start_run():
    # Log the hyperparameters
    mlflow.log_params(rf_params)

    # Log the loss metric
    mlflow.log_metric("accuracy" ,rf_acc)
    mlflow.log_metric("MAE",rf_mae)
    mlflow.log_metric("MSE",rf_mse)
    mlflow.log_metric("F1 score",rf_f1)

    # Set a tag that we can use to remind ourselves what this run was for
    mlflow.set_tag("Training Info", "Random Forest model")

    # Log the model
    model_info = mlflow.sklearn.log_model(
        sk_model=rf,
        artifact_path="best_model",
        registered_model_name="Random Forest",
    )

# SVM

with mlflow.start_run():
#     Log the hyperparameters
    mlflow.log_params(svm_params)

#     Log the loss metric
    mlflow.log_metric("accuracy" ,svm_acc)
    mlflow.log_metric("MAE",svm_mae)
    mlflow.log_metric("MSE",svm_mse)
    mlflow.log_metric("F1 score",svm_f1)

#     Set a tag that we can use to remind ourselves what this run was for
    mlflow.set_tag("Training Info", "Random Forest model")

#     Log the model
    model_info = mlflow.sklearn.log_model(
        sk_model=SVC_model,
        artifact_path="2nd model",
        registered_model_name="Support vector machine",
    )

    mlflow.log_artifact(scaler)

