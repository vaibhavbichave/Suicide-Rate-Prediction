# Suicide Rate Prediction 
![image](https://user-images.githubusercontent.com/79131292/144252164-b6d936ff-001c-4b55-9728-3af3dfa2e6b4.png)
![image](https://user-images.githubusercontent.com/79131292/144252842-784ae6c7-951a-4ce6-acb2-8e23c4e2d780.png)

## Table of Content
  * [Introduction](#introduction)
  * [Installation](#installation)
  * [Directory Tree](#directory-tree)
  * [Result](#result)
  * [Conclusion](#conclusion)


## Introduction
Suicide is a serious public health problem. The World Health
Organization (WHO) estimates that every year close to 800 000 people
take their own life, which is one person every 40 seconds and there are
many more people who attempt suicide. Suicide occurs throughout the
lifespan and was the second leading cause of death among 25-35 year
olds globally in 2016.
Hence it is quite clear that suicide is a cause for global concern, so it
should be analyzed which are the contributing factors for suicide. Here
we have analyzed and visualized the factors affecting the suicide rate in
a certain region or country.

The objective of this project is to predict the suicide rates using Machine Learning algorithms and to analyzing 
significant patterns features that result in increase of suicide rates globally. To see project click [here](https://suicide-rate-prediction-api.herokuapp.com/).


## Installation
The Code is written in Python 3.6.10. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Directory Tree 
```
├── pickle
│   ├── label.pkl
│   ├── model.pkl
│   ├── robust.pkl
├── templates
│   ├── index.html
│   ├── styles.css
├── Procfile
├── README.md
├── Suicide Rate Prediction.ipynb
├── app.py
├── requirements.txt
├── suicide_data.csv

```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/3/31/NumPy_logo_2020.svg" width=200>](https://numpy.org/doc/) [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" width=200>](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg" width=100>](https://matplotlib.org/)
[<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) 
[<img target="_blank" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScq-xocLctL07Jy0tpR_p9w0Q42_rK1aAkNfW6sm3ucjFKWML39aaJPgdhadyCnEiK7vw&usqp=CAU" width=200>](https://flask.palletsprojects.com/en/2.0.x/) 

## Result

Accuracy of various model used for prediction
<br>

||ML Model|	Train Accuracy|	Test Accuracy|	Train RMSE|	Test RMSE|
|---|---|---|---|---|---|
0|	Bagging Regression|	0.999|	0.997|	0.240|	0.478|
1|	Random Forest|	0.991|	0.988	|0.903|	1.041|
2|	Gradient Boosted Regression|	0.991|	0.988|	0.925|	1.031|
3|	Decision Tree|	0.976|	0.969|	1.498|	1.653|
4|	Multilayer Perceptron Regression	|0.894|	0.902|	3.144|	2.935|
5|	k-Nearest Neighbors Regression|	1.000|	0.732|	0.000|	4.862|
6|	Linear Regression	|0.284|	0.274|	8.179|	8.006|
7|	Support Vector Regression|	0.212	|0.207|	8.579|	8.367|

<br>

Accuracy of Bagging Regression by changing n_estimators value 
<br><br>
![image](https://user-images.githubusercontent.com/79131292/144249597-86d84518-844d-491d-a70d-02cac811e9a8.png)



## Conclusion
The final take away form this project is the working of different machine learning models on a dataset and understanding their parameters. Creating this notebook helped me to learn a lot about the parameters of the models, how to tuned them and how they affect the model performance. The final conclusion on the suicide dataset are that the irrespective of age group and generation, male population are more prone to commit suicide than female.
