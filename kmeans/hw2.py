import numpy as np 
import pandas as pd
from scipy.spatial import distance
import sklearn
from sklearn.cluster import KMeans


def my_kmeans(nparray, k, random_state):
    df = pd.DataFrame(nparray)
    centers = (df.sample(k, random_state = random_state)).to_numpy()

    for item in range(k):
        cont = True
        while cont:
            distances = distance.cdist(nparray, centers, 'euclidean')
            labels = np.argmin(distances, axis=1) #labels just means clusters here
            current_ind = labels == item
            subset = nparray[current_ind,:]
            subset_mean = np.mean(subset, axis=0)
            if np.all([subset_mean[0],subset_mean[1]] == centers[item]):
                cont = False
            else:
                centers[item] = [subset_mean[0],subset_mean[1]]
    
    return centers, labels


def within_sum_of_squares(data, k):
    total = 0

    km_alg_norm = KMeans(n_clusters=k, init="random",random_state = 1, max_iter = 200)
    fit2 = km_alg_norm.fit(data) 

    for i in range (0, k):
        cluster_center = [fit2.cluster_centers_[i]]
        inds = (fit2.labels_ == i)
        cluster_points = data[inds,:]
        
        cluster_spread = distance.cdist(cluster_points, cluster_center, 'euclidean')
        cluster_total = np.sum(cluster_spread)

        total += cluster_total
    return total


def looping_kmeans(nparray, kslist):
    list_of_goodness = []
    for k in kslist:
        km_alg = KMeans(n_clusters=k, init="random", random_state = 1, max_iter = 200)
        fit1 = km_alg.fit(nparray)
        goodness = within_sum_of_squares(nparray, k)
        list_of_goodness.append(goodness)
    print("list_of_goodness", list_of_goodness)
    return list_of_goodness
