# Homework 5
Welcome to your fifth homework assignment for CSC 294. In this 
assignment, we will practice implementing cross-validation. 

In this assignment, we will use a dataset similar to our (fake) 
employee dataset, encoded in the `hw5data.csv` file. In this data 
set, there are four variables: a new hire's score on the big five 
personality test (`neuroticism`), their most recent performance score 
(`performance`), their job type (`job`), and their current salary. 
Our goal is to determine what relationship -- if any -- salary has 
with the other three variables. 

A few notes before we begin:
1. For this assignment, please submit your work in the jupyter 
   notebook called `hw5_notebook.ipynb`. 
2. There are unit tests for this assignment, so that you can check 
   that elements of your code work. Place these elements in the file 
   called `hw5.py`. Note that part of the assignment is showing that 
   the tests pass locally and on github actions. 

## Question 1: Pre-processing the data

Given that our implementations for linear regression assume that our 
data is in the form of a numpy array, we need to ensure that we can 
import our data as such. 

This means that we need to check that each column of our data 
contains numbers. If it does not, then we need to convert the 
information in those columns to numbers. For example, suppose that 
we have a variable of favorite colors with possible values `red`, 
`blue`, and `green`. We might convert this information such that 
`red` becomes 0, `blue` becomes 1, and `green` becomes 2. 

For this problem, create a function `data_wrangle` (in `hw5.py`) that 
will take an input `filename` and a list of columns from that dataset 
that need to be pre-processed into numerical values. Your function 
should:    
1. Import the data with `pandas` 
2. For each column listed as an input (ie. those with non-numerical 
   data):
   * Determine the unique values in that column
   * Convert the unique values in into unique numbers. 
3. Then the function should extract the data's column names from 
   the observation rows.  
4. The data should then be converted to a numpy array
5. Finally `data_wrangle` should output all of the column names in 
   order as well as the converted dataset. 

_Hint:_ If your tests are throwing odd errors, you may need to 
convert the `type` of your final numpy array using `.astype(float)`

## Question 2: Implement k-fold Cross-Validation

Create a function `kfold_CV` (in `hw5.py`) that implements k-fold 
cross-validation. 
The inputs, in order, should be:
1. The full dataset (as a numpy array)
2. The header list (as in the list of variable/column names, in the 
   the order that they appear in the dataset)
3. Input variables
4. Output variables
5. Value for _k_

Using these inputs, `kfold_CV` should extract the input and output 
variables from the full dataset, divide the data into the _k_ folds, 
determine the linear relationship for the output variable given the 
input variables for each fold, and then `kfold_CV` should output only 
the cross-validated error as a float. 

## Question 3: Use 10-fold Cross-Validation

Using your function from question 2, import `hw5.py` into your 
jupyter notebook. Now use `kfold_CV` to determine the shape of the 
"true" relationship for `salary`. 

Test the following combinations of input variables:
* `neuroticism`
* `performance`
* `job`
* `neuroticism` and `performance`
* `neuroticism` and `job`
* `performance` and `job`
* `neuroticism`, `performance` and `job`

Using 10-fold cross-val, choose which combination yields the best 
relationship for describing `salary` and justify your choice. Your 
justification should be about 3 to 6 sentences. 

As a note, your errors may be quite large. This is a _fake_ dataset 
and errors being on the order of 10^9 is not unexpected for this 
_fake_ dataset. 

## Question 4: Determine the full model

During cross-val, you used parts of the data in training 
and the rest in testing. We use cross-val to help us pick our model. 
Once you have determined what variables your model should include, 
find the actual coefficients for the model using all of the dataset. 
In 3 to 6 sentences, explain why using all of the data in the creation 
of the model is appropriate in this case. 

## Question 5: Tests passing 

For this question, please submit screenshots of your tests passing 
locally and on GitHubActions  

## Rubric

|  Q  | Topic                         | No Attempt | Partial | Complete | 
|-----|-----------------------------  |------------|---------|----------|
|  1  | Preprocess your data          |            |         |          |  
|  2  | Implement k-fold              |            |         |          |   
| ... | Can handle a variet of k's    |            |         |          |
|  3  | Apply k-fold to 7 different   |  --------- |  ------ |  ------  |
| ... |     combinations of variables |            |         |          | 
|  4  | Set the final model           |            |         |          |
| ... | Explain why you use all data  |            |         |          |
|  5  | Local tests                   |            |         |          |
| ... | GitHub Actions                |            |         |          |

|  Q  | Topic                         | Have questions about| Could again without help | 
|-----|-----------------------------  |---------------------|--------------------------|
|  1  | Preprocess your data          |                     |                          |  
|  2  | Implement k-fold              |                     |                          |   
| ... | Can handle a variet of k's    |                     |                          |
|  3  | Apply k-fold to 7 different   |  ------------------ |--------------------------|
| ... |     combinations of variables |                     |                          | 
|  4  | Set the final model           |                     |                          |
| ... | Explain why you use all data  |                     |                          |
|  5  | Local tests                   |                     |                          |
| ... | GitHub Actions                |                     |                          |



### Reminders
* Check your file names carefully. Be sure to set up your directory 
to ignore and connect when needed
* Any import statements should be at the top of your python files or 
in the first code block of a notebook. 

#### Resources Consulted for this homework
0. [Numpy isnan() fails on an array of floats (from pandas dataframe apply)](https://stackoverflow.com/questions/36000993/numpy-isnan-fails-on-an-array-of-floats-from-pandas-dataframe-apply)   
1. [How to get column names in Pandas dataframe](https://www.geeksforgeeks.org/how-to-get-column-names-in-pandas-dataframe/)   
