import mlflow
import pickle
from mlflow.models import infer_signature


#Load the model
best_model = pickle.load(open("/workspaces/MissedMatch/artifacts/model.pkl", 'rb'))
scaler = pickle.load(open("/workspaces/MissedMatch/artifacts/model.pkl", 'rb'))
 

# Define the model hyperparameters
params = {
    "solver": "lbfgs",
    "max_iter": 1000,
    "multi_class": "auto",
    "random_state": 8888,
}

# Train the model
rf = best_model

# Set our tracking server uri for logging
mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")

# Create a new MLflow Experiment
mlflow.set_experiment("MissedMatch")

# Start an MLflow run
with mlflow.start_run():
    # Log the hyperparameters
    mlflow.log_params(params)

    # Log the loss metric
    #mlflow.log_metric("accuracy", accuracy)

    # Set a tag that we can use to remind ourselves what this run was for
    mlflow.set_tag("Training Info", "Random Forest model")

    # Log the model
    model_info = mlflow.sklearn.log_model(
        sk_model=rf,
        artifact_path="best_model",
        registered_model_name="Random Forest",
    )

    # Log model artifact
    mlflow.log_artifact(rf)
    
    # Log scaler artifact
    mlflow.log_artifact(scaler)
