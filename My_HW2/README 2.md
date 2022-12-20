
Another important component of this work is evaluating the clusters. There are several ways to go about this, each with their own advantages. Some examples are Within Cluster Sum of Squares (WCSS) and Between Clusters Sum of Squares (BCSS). Within Cluster Sum of Squares is the total distance between each data point and the cluster center. It is calculated by finding the Euclidean distance between a point and its assigned centroid. This is calculated for every point. Then the values are summed and the sum is divided by the number of points. This will return an average for each cluster. Then, all of the cluter averages are averaged to produce the average Within Cluster Sum of Squares. Between Clusters Sum of Squares differs from this method in that it ____________. It is calculated by __________ [1]. 

In this assignment, only Within Cluster Sum of Squares is used




# Resources

[1] https://odsc.medium.com/unsupervised-learning-evaluating-clusters-bd47eed175ce


# Homework 2

Welcome to your second homework assignment for CSC 294. In this assignment, you will: 
* Write your own k-means
* Explore how to choose _k_
* Dicuss limits of k-means

**Note 1** - Given the stochastic nature of k-means, the unit tests will look a bit odd for 
the two coding questions. With your submission, include screenshots of the tests 
passing locally and on github actions. 

**Note 2** - For questions 2 and 3, please put your written answers and plots in a jupyter notebook. Your code should stay in `hw2.py`

## Question 1: Your k-means implementation 
For this question, you will submit your "cold" k-means implementation and include (either 
in your python file or in a jupyter notebook) your justification for the stopping 
condition(s) that you used in your implementations. Your implementation should be 
called `my_kmeans()` and should set at three inputs **in this order** -

* A numpy array
* The number of cluster (ie. _k_)
* The random_state

Your implementation should terminate with output including:
- The cluster centers
- Cluster labels for the data points

You may **not** use the `sklearn` implementation for kmeans in this question. 


## Question 2: Choosing _k_ using elbowology 
### Part A
In k-means, we supply the number of clusters that we believe our data has. This means that 
the choice of _k_ is made without being directly derived from the data. In this question, 
you will use _elbowology_ to determine the number of clusters that our data falls into. 

For this question, we will use the `students_info.csv` for this question. For each of the 
three variable combinations, please normalize your variables and then do the following:
* Using _within cluster sum of squares_ as the measure of 
  cluster "goodness", write a function `looping_kmeans` that perform k-means using `sklearn` 
  and computes the "goodness" of clusters for _k=1, k=2, ..., k=10._ While the k-means should 
  use the `sklearn` implementation, the measure of "goodness" should be written by you. 
  The inputs should be 1) a numpy array and list of values for _k_, with the output being the 
  list of the "goodness" measures. 
* Plot the values of _k_ against your chosen measure of cluster "goodness" as a line plot with 
  each point marked clearly. 
* Examining your plot, find the value of _k_ that is closest to the "elbow"; that is where the 
  plot changes directions most sharply. This point should look like the elbow on a bent arm.   
  
The variable combinations are:
1. Gym time and average cups of coffee
2. Sleep and GPA
4. All numerical variables within `students_info.csv`

Hint: You might write a pre-processing function that can take data and the column names as input and returns just the part of the data that you want

### Part B
Given your plots above, how many clusters do our students fall into. You must choose **one** 
number and justify your choice. 


## Question 3: Limitations of k-means
When working with a new method, we need to explore its limitations. For this question, we 
explore if k-means can work on all data. Considering three kinds of data, please explain 
if k-means can work on it. If you believe that it can, explain; and if not, offer a counter 
example. 
* _Numerical_ variables: data that is just numbers, such as human height or outdoor temperature
* _Categorical_ variables: data that is based on categories or classes, such as coffee/tea 
preferences or favorite color
* _Ordinal_ variables: data that is categorical with an agreed upon ordering such as birth month
 or seasons
 
 For each type, would k-means work? If yes, explain why. If not, provide a counter example. 

## Rubric

For each homework assignment, you will need to fill in two self-evaluation rubrics. During the feedback stage, the instructor will add a third rubric. To denote your choice, please add X(s) under the appropriate column(s): 

|  Q  | Topic                         | No Attempt | Partial | Complete | 
|-----|-----------------------------  |------------|---------|----------|
|  1  | Creating $k$-means...         |  ------    |  ------ |  ------  |  
| ... | Follows pseudo code (lab 3)   |            |         |          | 
| ... | Uses index trick              |            |         |          |   
| ... | Handles more than 2 groups    |            |         |          |  
|  2  | Measure of goodness           |            |         |          |
| ..  | Looping $k$means function     |            |         |          |
| ... | Selects $k$ from goodness for:|  --------- |  ------ |  ------  |
| ... | - different sets of variables |            |         |          |
| ... | - based on plots (part b)     |            |         |          |                
|  3  | Articulate limits of $k$-means|            |         |          |
|  4  | Local tests                   |            |         |          |
| ... | GitHub Actions                |            |         |          |


|  Q  | Topic                         | Have questions about| Could again without help | 
|-----|-----------------------------  |---------------------|--------------------------|
|  1  | Creating $k$-means...         |  -----------------  | ---------------------    |  
| ... | Follows pseudo code (lab 3)   |                     |                          |
| ... | Uses index trick              |                     |                          |  
| ... | Handles more than 2 groups    |                     |                          | 
|  2  | Measure of goodness           |                     |                          |  
| ..  | Looping $k$means function     |                     |                          | 
| ... | Selects $k$ from goodness for:|  -----------------  | ---------------------    | 
| ... | - different sets of variables |                     |                          | 
| ... | - based on plots (part b)     |                     |                          |
|  3  | Articulate limits of $k$-means|                     |                          | 
|  4  | Local tests                   |                     |                          | 
| ... | GitHub Actions                |                     |                          | 

### Reminders
* Check your file names carefully. Be sure to set up your directory to ignore and connect 
when needed
* Any import statements should be at the top of your python files or in the first 
code block of a notebook. 

#### Resources consulted in creating this homework
0. _Python for Data Analysis_
1. [Empirical evaluation of the impact of k-means initialization](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.html#sphx-glr-auto-examples-cluster-plot-kmeans-stability-low-dim-dense-py)
2. [How to Slice Lists/Arrays and Tuples in Python](https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/)
