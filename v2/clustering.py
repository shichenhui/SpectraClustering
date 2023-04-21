import sys, os, time
import argparse
import pandas as pd
import numpy as np
import yaml
from collections import Counter
from ClusteringMethods import *
import dataLoad


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, help='The spectra dataset you want to choose.')
    parser.add_argument('--method', type=str, help='Clustering method.')
    parser.add_argument('--clusters', type=int, help='The number of clusters of clustering.', default=None)
    parser.add_argument('--pca', type=int,
                        help='Reduce dimension of data with PCA or not. 0 means no PCA, '
                             'other numbers means the dimension to reduce to.', default=0)

    return parser


def command_line_args(args):
    parser = parse_args()
    args, unknown = parser.parse_known_args(args)
    unknown_dict = dict(zip(unknown[::2], unknown[1::2]))
    return args, unknown_dict


def choose_method(method, clusters, parameters):
    if method == 'Kmeans':
        from sklearn.cluster import KMeans
        return KMeans(n_clusters=clusters, **parameters)
    elif method == 'GMM':
        from sklearn.mixture import GaussianMixture
        return GaussianMixture(n_components=clusters, **parameters)
    elif method == 'HierarchicalClustering':
        from sklearn.cluster import AgglomerativeClustering
        return AgglomerativeClustering(n_clusters=clusters, **parameters)
    elif method == 'CFSFDP':
        from ClusteringMethods.DPC import DPC
        return DPC(K=clusters, **parameters)
    elif method == 'Kmedoids':
        from ClusteringMethods.KCenters import KMedoid
        return KMedoid(k_num_center=clusters)
    elif method == 'DBSCAN':
        from sklearn.cluster import DBSCAN
        return DBSCAN(**parameters)
    elif method == 'SOM':
        from ClusteringMethods.SOM import SOM
        return SOM(n_clusters=clusters, dimensiom=data.shape[1], parameters=parameters)
    elif method == 'KmeansDP':
        from ClusteringMethods.KMeansDP import KMeansDP
        return KMeansDP(n_clusters=clusters, data=data, **parameters)


def calc_accuracy(y_true, y_predict):
    label_unique = np.unique(y_true)
    acc = 0
    for i in label_unique:
        r = Counter(y_predict[y_true == i])
        # The accuracy of class i, maybe false, depend on the Counter.
        acc_i = r.most_common(1)[0][1] / sum(y_true == i)
        print(r, acc_i)
        acc += acc_i
    print('average accuracy:', acc/len(label_unique))


def load_config():
    with open('./data_config.yml', encoding='utf-8') as file_config:
        data_config = yaml.load(file_config, Loader=yaml.FullLoader)
    with open('./parameters.yml', encoding='utf-8') as file_config:
        parameters = yaml.load(file_config, Loader=yaml.FullLoader)
        paras = {} if (parameters[arg.method] == None) else parameters[arg.method]
    return data_config[arg.dataset]['save_filename'], paras


def run(dataset, model):
    print('run', arg.method)
    t1 = time.time()
    y_pred = model.fit_predict(dataset)
    t2 = time.time()
    print('finish run, consume time:', t2 - t1)
    return y_pred


if __name__ == '__main__':
    # Get running parameters and parameters of clustering method.
    arg, parameters_input = command_line_args(sys.argv[1:])
    # Get config of datafile and default parameters of clustering methods.
    data_config, parameters = load_config()
    # Update parameters of clustering methods by user's input.
    parameters.update(parameters_input)
    print(arg)
    print('Other parameters of ', arg.method, parameters)

    data, label = dataLoad.load(filename=data_config, pca=arg.pca)
    #label = np.array([0] * 2000 + [1] * 2000 + [2] * 2000 + [3] * 2000)

    model = choose_method(arg.method, arg.clusters, parameters)
    y_pred = run(data, model)

    calc_accuracy(label, y_pred)
