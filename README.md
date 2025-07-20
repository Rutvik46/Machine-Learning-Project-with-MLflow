# Machine-Learning-Project-with-MLflow


## Workflows

1. Update config.yaml   
2. Update schema.yaml   # datasets columns with data type
3. Update params.yaml   # model parameters
4. Update the entity    
5. Update the configuration manager in src config
6. Update the components # ETL
7. Update the pipeline   # training and prediction pipeline
8. Update the main.py
9. Update the app.py


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Rutvik46/Machine-Learning-Project-with-MLflow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.11 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/Rutvik46/Machine-Learning-Project-with-MLflow.mlflow \
MLFLOW_TRACKING_USERNAME=Rutvik46 \
MLFLOW_TRACKING_PASSWORD=fdf9d63cdff88d1ed6fd22bc2f3d34a8c0672d1a \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Rutvik46/Machine-Learning-Project-with-MLflow

export MLFLOW_TRACKING_USERNAME=Rutvik46 

export MLFLOW_TRACKING_PASSWORD=fdf9d63cdff88d1ed6fd22bc2f3d34a8c0672d1a

```