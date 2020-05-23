import numpy as np

def getN(set1, set2):
    ''' output the number matrix n given to sets of clusters
    Parameter:
        set1: List of list --> [[observations in cluster 1], [.... in cluster 2], [....]]
        set2: same as list 2
    Returns:
        n: np matrix, number matrix
    '''
    n = np.zeros((len(set1), len(set2))) 
    for i in range(len(set1)):
        for elem in set1[i]: 
            for j in range(len(set2)):
                if elem in set2[j]:
                    n[i][j] += 1 
    return n

def getS(n):
    nFlat = n.flatten()
    S = 0
    for thing in nFlat:
        S += thing*(thing-1)/2
    return S

def getD(n):
    pass

def kMeans(observations, centers):
    obsShape = observations[0].shape[0]

    clusters = []
    distance = np.zeros(len(centers))
    means = np.zeros((len(centers), obsShape))
    newMeans = np.zeros((len(centers), obsShape))
    changed = True

    while changed:
        # init empty clusters
        for center in centers:
            cluster = []
            clusters.append(cluster)

        # loop through observations 
        for observation in observations:
            i = 0
            for center in centers:
                distance[i] = np.linalg.norm(observation-center) # calculate distance
                i += 1
            clusterIdx = np.argmin(distance) #assign to cluster 
            clusters[clusterIdx].append(observation) #add to cluster
        
        # calculate new means
        for i in range(len(centers)):
            newMeans[i] =  np.mean(clusters[i], axis=0)
            centers[i] = newMeans[i]
        
        # stopping condition
        for i in range(means.shape[0]):
            if (means[i] != newMeans[i]).all(): # if any of them are changed keep going
                break

        # nothing changed cluster, end loop
        changed = False

    # print final results
    print(centers)
    for cluster in clusters:
        print(cluster)
    return 



if __name__ == "__main__":
    centers = [[1, 1], [3.5, 3.5]]
    observations = np.asarray([[1,1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]])
    kMeans(observations, centers)
