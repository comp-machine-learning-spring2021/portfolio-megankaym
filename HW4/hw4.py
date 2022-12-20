import pytest
import pandas as pd
import numpy as np
import matplotlib as matlib

students = pd.read_csv("students_info.csv")
justtwo_np = students[["sleep","coffee"]].to_numpy()

def var_dataproj(data, direction):
    var_mat = np.dot(data, direction)**2
    return np.mean(var_mat)

def grad_var(data, direction):
    
    # Compute projections
    proj = np.dot(data,direction)
    
    # Compute helper constants
    dir_sq = np.dot(direction,direction)
    dir_mat = direction*np.ones(data.shape)
    
    # Compute derivative 
    data_mult = np.matlib.repmat(2*(dir_sq -2)*proj,2,1).T
    dir_mult = np.matlib.repmat(2*(proj**2),2,1).T
    
    grad_by_point = data_mult*data + dir_mult*dir_mat
    grad = np.sum(grad_by_point,axis = 0)
    
    return grad


# # Question 0

def remove_mean(data): #move to (0,0) aka mean center
    #nptable = data.to_numpy()
    mean_vec = np.mean(data, axis=0)
    table_std = data.copy() #shallow copy so technically i can return data or table_std (it doesnt matter)
    #but it looks better if u return table_std

    for i in range(data.shape[1]):
        table_std[:,i] = (data[:,i] - mean_vec[i]*np.ones(data.shape[0])) #take each column and take mean
    return table_std

# # Question 1

def unit_direction(w_vec):
    lennorm = np.linalg.norm(w_vec)
    result = (1/lennorm)*w_vec
    return result

def project_datapoint(blue, red_unit):
    projectionlen = (np.dot(blue, red_unit))/1 #len of red vector is 1
    if np.linalg.norm(red_unit) == 1:
        vecdir = unit_direction(red_unit)
        newvector = vecdir*projectionlen
        return newvector
    else:
        return 'not unit vector'

def project_data(data, red_unit):
    projecteddata = []
    for datapoint in data:
        thing = project_datapoint(datapoint, red_unit)
        projecteddata.append(thing)
    return np.asarray(projecteddata)

# # Question 2 
from scipy.spatial import distance
def mse_n_dim(data_mc, data_rep):
    mse = (distance.cdist(data_mc, data_rep, 'euclidean'))**2
    meanmse = np.mean(mse)
    return meanmse

# # Question 3 
#  everything is in the jupyter notebook


## Question 4 
def first_comp(data_mc,step_max):
    L = 0.01 #fixed learning rate
    outmse = []
    p_1 = -1
    p_2 = 0
    vector1 = np.array((p_1, p_2))
    
    for stp in range(step_max):
        data_rep = project_data(data_mc, vector1)
        mse = mse_n_dim(data_mc, data_rep)
        outmse.append(mse)
        
    grad_var(outmse, vector1)
    return vector1