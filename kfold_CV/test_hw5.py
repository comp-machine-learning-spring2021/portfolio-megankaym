import pytest
import pandas as pd
import numpy as np
from sklearn import linear_model

import hw5

hw_data = pd.read_csv("hw5data.csv")

# Question 1

def test_data_wrangle_len():
	out = hw5.data_wrangle("hw5data.csv",['job'])
	assert len(out) == 2

def test_data_wrangle_type():
	out = hw5.data_wrangle("hw5data.csv",['job'])
	assert type(out) == type((3,2))

def test_data_wrangle_data():
	out = hw5.data_wrangle("hw5data.csv",['job'])[1]
	assert np.sum(np.isnan(out)) == 0

# Question 2

def test_kfold_CV_type():
	cols = ['neuroticism', 'performance', 'job', 'salary']
	data_np = hw5.data_wrangle("hw5data.csv",['job'])[1]
	CV = hw5.kfold_CV(data_np, cols, ['job'], 'salary',12)
	assert isinstance(CV, float) 

def test_kfold_CV_shape():
	cols = ['neuroticism', 'performance', 'job', 'salary']
	data_np = hw5.data_wrangle("hw5data.csv",['job'])[1]
	CV = hw5.kfold_CV(data_np, cols, ['job'], 'salary',12)

	expected = 1
	assert len([CV]) == expected
