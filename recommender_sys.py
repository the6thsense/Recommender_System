# -*- coding: utf-8 -*-
"""Recommender_sys.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GLugp6jZRiG8ls1mvlHL1x8Z-0b1zwoD
"""

!pip install -q kaggle

a = [1]
while(1):
    a.extend(a)

from google.colab import files

!ls -lt

cd /root/.kaggle

cd /root/.kaggle

files.upload()

!ls -lt



!kaggle competitions download -c https://www.kaggle.com/grouplens/movielens-20m-dataset/download







! chmod 600 /root/.kaggle/kaggle.json

!kaggle datasets download -d grouplens/movielens-20m-dataset

import pandas as pd
import numpy as np
import sklearn as skl
from sklearn.preprocessing import scale, PolynomialFeatures
from sklearn.model_selection import cross_val_score
from sklearn.metrics import  mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, RidgeCV, Lasso, LassoCV

import statsmodels.formula.api as smf



from zipfile import ZipFile

zipper = ZipFile( "movielens-20m-dataset.zip")
files = zipper.infolist()


with ZipFile( "movielens-20m-dataset.zip", 'r') as zip_ref:
    zip_ref.extractall("/root/.kaggle")



ls -lt

tags = pd.read_csv( "tag.csv")
rating = pd.read_csv( "rating.csv")
movie = pd.read_csv( "movie.csv")



tags.head()

movie.head()

tags = tags.merge(rating, on ="movieId")

tags.head()

link.tail()

ratings = pd.DataFrame(rating.groupby( "movieId").mean()["rating"])

ratings["rating"] = pd.Series(rating.rating.astype(float))

count_mId = rating.groupby('movieId').count()
mean_mId = rating.groupby("movieId").mean()
mean_mId

measure_index = pd.DataFrame(mean_mId.rating*count_mId.rating)
measure_index.head()

rating.head()

tags.sort_index()

import matplotlib.pyplot as plt
plt.plot( measure_index )

tags = tags.groupby("movieId").count().sort_index()

tags.head()

tags = tags.merge(measure_index, on = "movieId")
tags.head()

tags.columns = ["userId","tag","timestamp","title","genres","measure_index"]

tags.head()

to_compare = tags.measure_index.sort_values(ascending = False)

to_compare = pd.DataFrame(to_compare)

to_compare.head()

