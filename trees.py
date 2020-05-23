import numpy as np

def calcPurityGain(root, branches):
    nRoot = np.sum(root)
    iRoot = calcImpurity(root)
    branchSum = 0
    
    for branch in branches:
        iBranch = np.sum(branch)/nRoot*calcImpurity(branch)
        branchSum += iBranch
    return iRoot - branchSum

def calcImpurity(branch):
    p = np.max(branch)/np.sum(branch)
    return 1 - p

def getTreeAcc(root, branches):
    nRoot = np.sum(root)
    nominator = 0
    for branch in branches:
        nominator += np.max(branch)
    
    return nominator/nRoot 


if __name__ == "__main__":
    root = np.asarray([263, 359, 358])
    branches1 = np.asarray([[143, 137, 54], [120, 222, 304]])
    branches2 = np.asarray([[223, 251, 197], [40, 108, 161]])
    impurity = calcPurityGain(root, branches1)
    print(impurity)
    acc = getTreeAcc(root, branches2)
    print(acc)

