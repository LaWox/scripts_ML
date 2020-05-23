import numpy as np
from operator import itemgetter

def varianceExplained(numerator, denomenator):
    numerator = np.asarray(numerator) 
    denomenator = np.asarray(denomenator)

    return (np.sum(np.power(numerator, 2))/np.sum(np.power(denomenator, 2)))

def projectVectors(projecte, projectedOn):
    return projectedOn@projecte

if __name__ == "__main__":
    denom = [14.4,  11.41, 9.46, 4.19, 0.17]  
    num = [0, 1, 2]
    num = itemgetter(*num)(denom)

    vec1 = np.array([0.1, 0.5, 0.5, 0.5, 0.9])
    vec2 = np.array([0.94, 0.01, -0.01, 0.11, -0.33])
    print(projectVectors(vec1, vec2))