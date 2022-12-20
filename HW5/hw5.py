import pandas as pd
import numpy as np
from sklearn import linear_model
import math

def compute_mse(truth_vec, predict_vec):
    return np.mean((truth_vec - predict_vec)**2)



def data_wrangle(dataset_file, lst):
    #extract data from the input file
    data = pd.read_csv(dataset_file)
    for col in lst:
        #counter for new numerical values
        count = 0
        
        #Determine the unique values in that column
        unique_values = data[col].unique()
        
        #replace our object type values to be numerical
        
        for val in unique_values:
            data.replace(to_replace = {col:val}, value = count, inplace = True)
            count += 1 #update count
    col_names = list(data.columns)
    data = data.to_numpy()
    return col_names, data



def kfold_CV(data, col_names, inputs, outputs, k):

    #extract the input and output variables from the full dataset
    inputdata = []
    for input in inputs:
        ind = col_names.index(input)
        inputdata.append(data[ind])

    outputdata = []
    #if outputs was a list instead of a string :)
    #for output in outputs:
    #    ind = col_names.index(output)
    #    outputdata.append(data[ind])
    #instead, since the input for outputs is just a string, we'll use this:
    outputdata.append(data[:,-1])

    #divide the data into the k folds. split_dataframes is a list of the data sections now
    split_dataframes = []
    index_to_split = len(data) // k
    start = 0
    end = index_to_split
    for split in range(k):
        temporary_df = data[start:end, :]
        split_dataframes.append(temporary_df)
        start += index_to_split
        end += index_to_split
    
    
    #output only the cross-validated error as a float #from lab 13
    # Initialize the list of errors
    test_errors = []

    # Loop over all points in the data set, letting each act as the test set
    for split in split_dataframes:

        # Split data into train and test
        test_data = split.T
        train_data = split_dataframes - split
        #train_data = list(set(test_data.tolist()).difference(set(train_data.tolist())))
        train_data = np.vstack(train_data).T
        #print("=======================test_data", test_data.shape, test_data)
        #print("=======================train_data", train_data.shape, train_data)
        
        
        # Create, train, predict, and compute mse
        test_errors = []
        lm = linear_model.LinearRegression()
        #print("TRAIN DATA SHAPE: ", train_data.T.shape)
        #print("TEST DATA SHAPE: ", test_data.T.shape)
        mod = lm.fit(test_data, train_data)

        test_preds = mod.predict(test_data)
        test_error = compute_mse(test_preds.T, test_data.T[-1])
        test_errors.append(test_error)
        
    # Compute the cross-val error
    return np.mean(test_errors)


#cols = ['neuroticism', 'performance', 'job', 'salary']
#data_np = data_wrangle("hw5data.csv",['job'])[1]
#CV = kfold_CV(data_np, cols, ['job'], 'salary',12)