# MissedMatch

## MLflow
to run the experimental in mlops you have to follow these steps

`pip install -r requirements`

`mlflow ui` or `python -m mlflow ui`

then you can run the main file 

`python main.py`

or you can run the train.py file

`python src/train.py`

you can look at another file called train_artifatcs, in this file you can run the model from the artifacts directly and provide it in your mlflow environment

`python src/train_artifacts.py`

to register your model you can use `register_model.py` file which contains how to register your model by adding the run id
you can find the run id through this path in mlflow 

**open mlflow env >> choose the model >> overview >> Details >> Run ID**

## Streamlit app

The streamlit app hosted in the streamlit cloud and you can run it through this link:

https://missedmatch.streamlit.app/

### Streamlit app code
You can have a look in the streamlit-app folder, in this folder you will find `app.py` which is the main file and the pages folder which contains `analysis.py ` , `home.py` and `prediction.py`
