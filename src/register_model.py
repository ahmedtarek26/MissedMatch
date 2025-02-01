import mlflow

model_name="Random Forest"
run_id = input('Enter run id :')
model_uri = f"runs:/{run_id}/{model_name}"

mlflow.register_model(
    model_uri, model_name
)