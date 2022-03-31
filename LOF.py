import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor
from scipy import stats

data_special = pd.read_csv('/home/shichenhui/code/spectra_clustering/data/special.csv',header = None)
data_usual = np.loadtxt('/home/shichenhui/code/spectra_clustering/data/'+'10-/star_AFGK_5wx4.csv', delimiter=',')


data_special_choose = data_special[data_special.iloc[:, 0] == 'Carbon'].iloc[:, 3:].values


print(data_usual.shape)
print(data_special_choose.shape)
data = np.concatenate([data_usual[:10000], data_special_choose[:100]])


clf = LocalOutlierFactor(n_neighbors=35, contamination=0.05)
y_pred = clf.fit_predict(data)

print(y_pred)
print(np.sum(y_pred[:10000]==-1))
print(np.sum(y_pred[-100:]==-1))