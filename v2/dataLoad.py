import sys, os,time
import pandas as pd
import numpy as np
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA


def load(filename, pca, norm=True):
    print('loading data:', filename)
    data = np.loadtxt(filename, delimiter=',')
    print('finish load')
    label = data[:,-1]
    data = data[:,:-1]

    if 'para' in filename:
        pass
    else:
        data = normalize(data)

    if pca != 0:
        print('PCA:', pca)
        pca = PCA(n_components=pca)
        data = pca.fit_transform(data)
        print(pca.explained_variance_ratio_.sum())

    return data, label

