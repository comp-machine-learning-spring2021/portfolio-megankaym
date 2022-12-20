import numpy as np 
import pandas as pd
from scipy.spatial import distance
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


#def within_sum_of_squares():


def looping_kmeans(nparray, kslist):
    print("kslist", kslist)
    #make array to keep track of corresponding values for each k. loop through each k value
    #and do k means on them to get the centers with that k
    #then fit data to that kmeans thing
    for k in kslist:
        km_alg = KMeans(n_clusters=k, init="random", random_state = 1, max_iter = 200)
        fit1 = km_alg.fit(nparray)
        cluster_centers = fit1.cluster_centers_
        print("cluster_centers", cluster_centers)
        label = km_alg.predict(np.array([[1,2]]))
        print("label", label)

    return cluster_centers
