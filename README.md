[![AutoML build passing](https://github.com/mxm32/automl/actions/workflows/main.yml/badge.svg)](https://github.com/mxm32/automl/actions/workflows/main.yml)


## AIPI 561: Project 2
# AutoML Classification

# FLAML AutoML

FLAML (Fast and Lightweight AutoML) is a lightweight Python library that finds accurate machine learning models automatically, efficiently and economically. It frees users from selecting learners and hyperparameters for each learner.
[FLAML documentation](https://microsoft.github.io/FLAML/docs/Getting-Started)

![flaml](https://user-images.githubusercontent.com/88257891/182977065-5f31cde7-9490-45c3-a9fc-b75a100124cf.png)

## FLAML for Classification:
For common machine learning tasks like classification and regression, it quickly finds quality models for user-provided data with low computational resources. It supports both classifcal machine learning models and deep neural networks.
[Source](https://github.com/microsoft/FLAML)

## Dataset
In this project, the "Iris" dataset, commonly used in classification machine learning demonstrations, was selected for implementing AutoML classification.

[Reference](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html)

This data sets consists of 3 different types of irises’ (Setosa, Versicolour, and Virginica) petal and sepal length, stored in a 150x4 numpy.ndarray. The rows are the samples and the columns are: Sepal Length, Sepal Width, Petal Length and Petal Width.

![Iris_virginica](https://user-images.githubusercontent.com/88257891/182976616-a181fe70-eaff-4b19-8bbd-8ee16d51ea34.jpg)
![Iris_dataset_scatterplot svg](https://user-images.githubusercontent.com/88257891/182976620-d6fa4da8-0b2b-4364-9785-a14005461cef.png)



## Getting Started

Create a virtual environment

```
python3 -m venv venv
```

Activate the virtual environment
  
```
source venv/bin/activate
```

Deploy
```
make all
```

## Usage
```
python3 main.py
```


## Results:

### Best model: [LGBM Classifier](https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMClassifier.html)

Time taken to find the best model: 0.5975360870361328

LGBMClassifier(colsample_bytree=0.9712608239851066,
               learning_rate=0.5066472382072831, max_bin=63,
               min_child_samples=9, n_estimators=4, num_leaves=4,
               reg_alpha=0.008673969948933881, reg_lambda=0.47452813352268625,
               verbose=-1)


## Full Output:

```
[flaml.automl: 08-04 23:16:09] {2444} INFO - task = classification
INFO:flaml.automl:task = classification
[flaml.automl: 08-04 23:16:09] {2446} INFO - Data split method: stratified
INFO:flaml.automl:Data split method: stratified
[flaml.automl: 08-04 23:16:09] {2449} INFO - Evaluation method: cv
INFO:flaml.automl:Evaluation method: cv
[flaml.automl: 08-04 23:16:09] {2568} INFO - Minimizing error metric: 1-accuracy
INFO:flaml.automl:Minimizing error metric: 1-accuracy
[flaml.automl: 08-04 23:16:09] {2708} INFO - List of ML learners in AutoML Run: ['lgbm', 'rf', 'catboost', 'xgboost', 'extra_tree', 'xgb_limitdepth', 'lrl1']
INFO:flaml.automl:List of ML learners in AutoML Run: ['lgbm', 'rf', 'catboost', 'xgboost', 'extra_tree', 'xgb_limitdepth', 'lrl1']
[flaml.automl: 08-04 23:16:09] {3010} INFO - iteration 0, current learner lgbm
INFO:flaml.automl:iteration 0, current learner lgbm
[flaml.automl: 08-04 23:16:09] {3144} INFO - Estimated sufficient time budget=781s. Estimated necessary time budget=19s.
INFO:flaml.automl:Estimated sufficient time budget=781s. Estimated necessary time budget=19s.
[flaml.automl: 08-04 23:16:09] {3196} INFO -  at 0.2s,	estimator lgbm's best error=0.0733,	best estimator lgbm's best error=0.0733
INFO:flaml.automl: at 0.2s,	estimator lgbm's best error=0.0733,	best estimator lgbm's best error=0.0733
[flaml.automl: 08-04 23:16:09] {3010} INFO - iteration 1, current learner lgbm
INFO:flaml.automl:iteration 1, current learner lgbm
[flaml.automl: 08-04 23:16:09] {3196} INFO -  at 0.2s,	estimator lgbm's best error=0.0733,	best estimator lgbm's best error=0.0733
INFO:flaml.automl: at 0.2s,	estimator lgbm's best error=0.0733,	best estimator lgbm's best error=0.0733
[flaml.automl: 08-04 23:16:09] {3010} INFO - iteration 2, current learner lgbm
INFO:flaml.automl:iteration 2, current learner lgbm
[flaml.automl: 08-04 23:16:09] {3196} INFO -  at 0.3s,	estimator lgbm's best error=0.0533,	best estimator lgbm's best error=0.0533
INFO:flaml.automl: at 0.3s,	estimator lgbm's best error=0.0533,	best estimator lgbm's best error=0.0533
[flaml.automl: 08-04 23:16:09] {3010} INFO - iteration 3, current learner lgbm
INFO:flaml.automl:iteration 3, current learner lgbm
[flaml.automl: 08-04 23:16:09] {3196} INFO -  at 0.4s,	estimator lgbm's best error=0.0533,	best estimator lgbm's best error=0.0533
INFO:flaml.automl: at 0.4s,	estimator lgbm's best error=0.0533,	best estimator lgbm's best error=0.0533
[flaml.automl: 08-04 23:16:09] {3010} INFO - iteration 4, current learner lgbm
INFO:flaml.automl:iteration 4, current learner lgbm
[flaml.automl: 08-04 23:16:09] {3196} INFO -  at 0.4s,	estimator lgbm's best error=0.0533,	best estimator lgbm's best error=0.0533
INFO:flaml.automl: at 0.4s,	estimator lgbm's best error=0.0533,	best estimator lgbm's best error=0.0533
[flaml.automl: 08-04 23:16:09] {3010} INFO - iteration 5, current learner lgbm
INFO:flaml.automl:iteration 5, current learner lgbm
[flaml.automl: 08-04 23:16:09] {3196} INFO -  at 0.5s,	estimator lgbm's best error=0.0467,	best estimator lgbm's best error=0.0467
INFO:flaml.automl: at 0.5s,	estimator lgbm's best error=0.0467,	best estimator lgbm's best error=0.0467
[flaml.automl: 08-04 23:16:09] {3010} INFO - iteration 6, current learner lgbm
INFO:flaml.automl:iteration 6, current learner lgbm
[flaml.automl: 08-04 23:16:09] {3196} INFO -  at 0.5s,	estimator lgbm's best error=0.0467,	best estimator lgbm's best error=0.0467
INFO:flaml.automl: at 0.5s,	estimator lgbm's best error=0.0467,	best estimator lgbm's best error=0.0467
[flaml.automl: 08-04 23:16:09] {3010} INFO - iteration 7, current learner lgbm
INFO:flaml.automl:iteration 7, current learner lgbm
[flaml.automl: 08-04 23:16:10] {3196} INFO -  at 0.6s,	estimator lgbm's best error=0.0400,	best estimator lgbm's best error=0.0400
INFO:flaml.automl: at 0.6s,	estimator lgbm's best error=0.0400,	best estimator lgbm's best error=0.0400
[flaml.automl: 08-04 23:16:10] {3010} INFO - iteration 8, current learner lgbm
INFO:flaml.automl:iteration 8, current learner lgbm
[flaml.automl: 08-04 23:16:10] {3196} INFO -  at 0.7s,	estimator lgbm's best error=0.0400,	best estimator lgbm's best error=0.0400
INFO:flaml.automl: at 0.7s,	estimator lgbm's best error=0.0400,	best estimator lgbm's best error=0.0400
[flaml.automl: 08-04 23:16:10] {3010} INFO - iteration 9, current learner lgbm
INFO:flaml.automl:iteration 9, current learner lgbm
[flaml.automl: 08-04 23:16:10] {3196} INFO -  at 0.7s,	estimator lgbm's best error=0.0400,	best estimator lgbm's best error=0.0400
INFO:flaml.automl: at 0.7s,	estimator lgbm's best error=0.0400,	best estimator lgbm's best error=0.0400
[flaml.automl: 08-04 23:16:10] {3010} INFO - iteration 10, current learner lgbm
INFO:flaml.automl:iteration 10, current learner lgbm
[flaml.automl: 08-04 23:16:10] {3196} INFO -  at 0.8s,	estimator lgbm's best error=0.0400,	best estimator lgbm's best error=0.0400
INFO:flaml.automl: at 0.8s,	estimator lgbm's best error=0.0400,	best estimator lgbm's best error=0.0400
[flaml.automl: 08-04 23:16:10] {3010} INFO - iteration 11, current learner xgboost
INFO:flaml.automl:iteration 11, current learner xgboost
[flaml.automl: 08-04 23:16:10] {3196} INFO -  at 1.0s,	estimator xgboost's best error=0.0600,	best estimator lgbm's best error=0.0400
INFO:flaml.automl: at 1.0s,	estimator xgboost's best error=0.0600,	best estimator lgbm's best error=0.0400
[flaml.automl: 08-04 23:16:10] {3456} INFO - retrain lgbm for 0.0s
INFO:flaml.automl:retrain lgbm for 0.0s
[flaml.automl: 08-04 23:16:10] {3461} INFO - retrained model: LGBMClassifier(colsample_bytree=0.9712608239851066,
               learning_rate=0.5066472382072831, max_bin=63,
               min_child_samples=9, n_estimators=4, num_leaves=4,
               reg_alpha=0.008673969948933881, reg_lambda=0.47452813352268625,
               verbose=-1)
INFO:flaml.automl:retrained model: LGBMClassifier(colsample_bytree=0.9712608239851066,
               learning_rate=0.5066472382072831, max_bin=63,
               min_child_samples=9, n_estimators=4, num_leaves=4,
               reg_alpha=0.008673969948933881, reg_lambda=0.47452813352268625,
               verbose=-1)
{2741} INFO - Time taken to find the best model: 0.5975360870361328
INFO:flaml.automl:Time taken to find the best model: 0.5975360870361328


LGBMClassifier(colsample_bytree=0.9712608239851066,
               learning_rate=0.5066472382072831, max_bin=63,
               min_child_samples=9, n_estimators=4, num_leaves=4,
               reg_alpha=0.008673969948933881, reg_lambda=0.47452813352268625,
               verbose=-1)
```
