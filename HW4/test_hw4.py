import pytest
import pandas as pd
import numpy as np
import numpy.matlib
import hw4

students = pd.read_csv("students_info.csv")
justtwo_np = students[["sleep","coffee"]].to_numpy()

red = np.array([1,1,1])
pink = (1/np.sqrt(3))*np.array([1,1,1])
blue = np.array([3,4,5])
purp = 12/np.sqrt(3)

pink2 = (1/np.sqrt(2))*np.array([1,1])

test_R = np.random.rand(100,3)


## Question 0

def test_remove_mean_shape():
	global justtwo_np

	expected = justtwo_np.shape
	out = hw4.remove_mean(justtwo_np)
	assert out.shape == expected

def test_remove_mean_mean():
	global justtwo_np

	expected = np.zeros(2)
	out_mean = np.mean(hw4.remove_mean(justtwo_np))
	assert np.allclose(out_mean, expected)

def test_remove_mean_sd():
	global justtwo_np

	expected = np.std(justtwo_np, axis = 0)
	out_sd = np.std(hw4.remove_mean(justtwo_np), axis = 0)
	assert np.allclose(expected, out_sd)


## Question 1

def test_unit_direction_type():
	global red
	expected = type(red)
	assert type(hw4.unit_direction(red)) == expected

def test_unit_direction():
	global red
	expected = (1/np.sqrt(3))*red
	assert np.allclose(hw4.unit_direction(red),expected)

def test_project_datapoint_type():
	global blue, pink

	expected = type(justtwo_np)
	assert type(hw4.project_datapoint(blue, pink)) == expected

def test_project_datapoint_shape():
	global blue, pink

	expected = pink.shape
	assert hw4.project_datapoint(blue, pink).shape == expected

def test_project_datapoint_values():
	global blue, pink

	purp = 12/np.sqrt(3)
	expected = purp*pink
	assert np.allclose(hw4.project_datapoint(blue, pink), expected)

def test_project_data_type():
	global test_R
	test_R_no_mean = hw4.remove_mean(test_R)

	expected = type(test_R)
	assert type(hw4.project_data(test_R_no_mean,pink)) == expected

def test_project_data_shape():
	global test_R
	test_R_no_mean = hw4.remove_mean(test_R)

	expected = test_R.shape
	assert (hw4.project_data(test_R,pink)).shape == expected


## Question 2 

def test_mse_n_dim_shape():
	global test_R 

	expected = 0
	guess = hw4.project_data(test_R,pink)

	out = hw4.mse_n_dim(test_R,guess)
	assert len(out.shape) == expected

def test_mse_n_dim_type():
	global test_R 

	expected = np.sum(test_R)
	guess = hw4.project_data(test_R,pink)

	out = hw4.mse_n_dim(test_R,guess)
	assert type(out) == type(expected)


## Question 4

def test_first_comp_type():
	global justtwo_np

	assert isinstance(hw4.first_comp(justtwo_np, 5000), tuple)

def test_first_comp_size():
	global justtwo_np
	
	assert len(hw4.first_comp(justtwo_np, 5000)) == 2

def test_first_comp_comp_size():
	global justtwo_np
	
	expected = (2,)
	out = hw4.first_comp(justtwo_np, 5000)[0]
	assert out.shape == expected

def test_first_comp_proj_size():
	global justtwo_np
	
	expected = justtwo_np.shape
	project_size = hw4.first_comp(justtwo_np, 5000)[1].shape 
	assert project_size == expected


