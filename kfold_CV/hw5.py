import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def compute_mse(truth_vec, predict_vec):
    return np.mean((truth_vec - predict_vec)**2)

def classify(pred, ans):
    incorrect = np.sum(ans[:] != pred[:])
    return np.mean(incorrect/ans.shape[0])

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
				

def kfold_CV(data, col_names, inputs, output, k):
    split_dataframe = np.array_split(data, k)
    mylist = []
    for x in inputs:
        start = col_names.index(x)
        mylist.append(start)
    end = col_names.index(output)
    
    cverror = []
    for i in range(k):
        test = split_dataframe.pop(i)
        train = np.vstack(split_dataframe)

        dt = DecisionTreeClassifier(ccp_alpha = 0.001, max_depth=5)
        dt.fit(train[:, mylist], train[:, end].astype(int))
        predictions = dt.predict(test[:, mylist])
        cverror.append(classify(predictions, test[:, [end]]))
        split_dataframe.insert(i, test)
    return np.mean(cverror)




#tests

# neuroticism

cols = ['neuroticism', 'salary']
data_np = data_wrangle("hw5data.csv",['neuroticism'])[1]
CV = kfold_CV(data_np, cols, ['neuroticism'], 'salary', 5)
print("neuroticism", CV)

# performance

cols = ['neuroticism', 'performance', 'job', 'salary']
data_np = data_wrangle("hw5data.csv",['performance'])[1]
CV = kfold_CV(data_np, cols, ['performance'], 'salary', 5)
print("performance", CV)

# job

cols = ['neuroticism', 'performance', 'job', 'salary']
data_np = data_wrangle("hw5data.csv",['job'])[1]
CV = kfold_CV(data_np, cols, ['job'], 'salary', 5)
print("job", CV)

# neuroticism & performance

cols = ['neuroticism', 'performance', 'job', 'salary']
data_np = data_wrangle("hw5data.csv",['neuroticism', 'performance'])[1]
CV = kfold_CV(data_np, cols, ['neuroticism', 'performance'], 'salary', 5)
print("neuroticism & performance", CV)

# neuroticism & job

cols = ['neuroticism', 'performance', 'job', 'salary']
data_np = data_wrangle("hw5data.csv",['neuroticism', 'job'])[1]
CV = kfold_CV(data_np, cols, ['neuroticism', 'job'], 'salary', 5)
print("neuroticism & job", CV)

# performance & job

cols = ['neuroticism', 'performance', 'job', 'salary']
data_np = data_wrangle("hw5data.csv",['performance', 'job'])[1]
CV = kfold_CV(data_np, cols, ['performance', 'job'], 'salary', 5)
print("performance & job", CV)

# neuroticism & performance & job

cols = ['neuroticism', 'performance', 'job', 'salary']
data_np = data_wrangle("hw5data.csv",['neuroticism', 'performance', 'job'])[1]
CV = kfold_CV(data_np, cols, ['neuroticism', 'performance', 'job'], 'salary', 5)
print("neuroticism & performance & job", CV)