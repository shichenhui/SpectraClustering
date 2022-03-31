from sklearn.cluster import DBSCAN
import sys, time
from sklearn.preprocessing import normalize
from collections import Counter
sys.path.append("..")
import DataLoader, Plot
from sklearn.decomposition import KernelPCA



data = DataLoader.load_spectra_from_csv('../data/spectra_all_proprocessed.csv')
Plot.plot_spectra(data[0:10])

print('pca...')
pca = KernelPCA(kernel='rbf',n_components=15,gamma=0.005)
pca.fit(data)
data = pca.fit_transform(data)

print('clustering...')
t1 = time.time()
y_pred = DBSCAN(eps = 0.1,min_samples=5, metric='manhattan').fit_predict(data)
t2 = time.time()

print(t2-t1)
print(Counter(y_pred[0:1000]))
print(Counter(y_pred[1001:2000]))
print(Counter(y_pred[2001:3000]))