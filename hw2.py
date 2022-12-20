import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.spatial import distance


def my_kmeans(nparray, k, random_state):
    df = pd.DataFrame(nparray)
    centers = (df.sample(k, random_state = random_state)).to_numpy()


    for item in range(k):
        cont = True
        while cont:
            distances = distance.cdist(nparray, centers, 'euclidean')
            labels = np.argmin(distances, axis=1)
            current_ind = labels == item
            subset = nparray[current_ind,:]
            subset_mean = np.mean(subset, axis=0)
            if np.all([subset_mean[0],subset_mean[1]] == centers[item]):
                cont = False
            else:
                centers[item] = [subset_mean[0],subset_mean[1]]
    

    return centers, labels

#def looping_kmeans(nparray, kslist):
#    get_data = nparray[]






"""def my_kmeans(nparray, k, random_state):
    df = pd.DataFrame(nparray)
    centers = (df.sample(k, random_state = random_state)).to_numpy()
    dists = distance.cdist(nparray, centers, 'euclidean')
    clusters = np.argmin(dists, axis=1)

    whole = []
    for item in range(k):
        inds = clusters == item
        points = []
        for i in inds:
            my_avg = np.mean([i for (i, x) in enumerate(inds) if x])
            points.append(my_avg)
        whole.append(points)
    
    dpoints = pd.DataFrame(whole)
    print(dpoints)


    #in this assignment, the labels are just numeric with index starting at 0
    labels = []
    for i in range(k):
        labels.append(i)


    return centers, labels"""