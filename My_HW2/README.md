kmeans is an unsupervised clustering method that to classifies unlabeled data by grouping them by features [1]. The output of a kmeans function is the centers (and labels) of the clusters. An important component of this work is developing a kmeans function from scratch so we can compare it to sklearn's own kmeans function. sklearn is a software machine learning Python library that enables programmers to implement pre-built functions [2]. 

Another important component of this work is evaluating the clusters. There are several ways to go about this, each with their own advantages. Some examples are Within Cluster Sum of Squares (WCSS) and Between Clusters Sum of Squares (BCSS). Within Cluster Sum of Squares is the total distance between each data point and the cluster center. It is calculated by finding the Euclidean distance between a point and its assigned centroid. This is calculated for every point. Then the values are summed and the sum is divided by the number of points. This will return an average for each cluster. Then, all of the cluter averages are averaged to produce the average Within Cluster Sum of Squares. Between Clusters Sum of Squares differs from this method in that it measures the squared average distance between all centroids. It is calculated by finding the Euclidean distance from a centroid to all other cluster centroids. This is calculated for every centroid. The values are then all summed together to achieve the Between Clusters Sum of Squares. To get the average Between Clusters Sum of Squares, you would divide by the number of centroids [3].  In this assignment, Within Cluster Sum of Squares is used.


# Results

After comparing my personal kmeans function coded from scratch with the sklearn kmeans function, it seems that my_kmeans took 4.15 ms ± 466 µs per loop (mean ± std. dev. of 10 runs, 15 loops each) and the CPU times were 6.56 ms, sys: 1.57 ms, total: 8.13 ms and the Wall time was 6.75 ms. The sklearn kmeans took 38.2 ms ± 4.2 ms per loop (mean ± std. dev. of 10 runs, 15 loops each) and the CPU times were 227 ms, sys: 31.3 ms, total: 258 ms and the Wall time was 56.4 ms. My implementation took less time than the sklearn implementation of kmeans. The memories, however, were very similar with my hand coded kmeans having a peak memory of 168.47 MiB and an increment of 0.26 MiB where the sklearn kmeans had a peak memory of 168.21 MiB and an increment of 0.09 MiB.

This coding component contributed insight to the time advantages of using a kmeans function from scratch as opposed to the built in sklearn function.

# Limitations of k-means

* _Numerical_ variables: data that is just numbers. kmeans can use numerical variables because you can mathematically compute the distances.
* _Categorical_ variables: data that is based on categories or classes. kmeans does not work with categorical data. for example, you can't compute euclidean distance with strings.
* _Ordinal_ variables: data that is categorical with an agreed upon ordering. kmeans can use ordinal variables, you would just have to map them to numerical variables.
 
 
 
# Resources

1. DeepAI. “K-Means.” DeepAI, DeepAI, 17 May 2019, https://deepai.org/machine-learning-glossary-and-terms/k-means. 

2. “Learn.” Scikit, https://scikit-learn.org/stable/. 

3. Science, ODSC - Open Data. “Unsupervised Learning: Evaluating Clusters.” Medium, Medium, 17 Dec. 2018, https://odsc.medium.com/unsupervised-learning-evaluating-clusters-bd47eed175ce. 
