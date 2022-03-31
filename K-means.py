from sklearn.cluster import KMeans
import time
from sklearn.preprocessing import normalize
from collections import Counter
import numpy as np
from sklearn.decomposition import PCA


print('加载数据')
t0 = time.time()
data = np.loadtxt(r'C:\Users\panda\Desktop\桌面备份\天体光谱\data\spectra_all_proprocessed.csv', delimiter=',')
t1 = time.time()
print('finished load data, consume time: ',t1-t0)

print('normalize data')
data = normalize(data)
pca = PCA(n_components=30)
data = pca.fit_transform(data)
print(pca.explained_variance_ratio_)
t2 = time.time()
print('finished normalize data, consume time:', t2-t1)


print('run k-means')
y_pred = KMeans(n_clusters=3).fit_predict(data)
t3 = time.time()

print('finished run model, consume time', t3-t2)

print(Counter(y_pred[0:1000]))
print(Counter(y_pred[1000:2000]))
print(Counter(y_pred[2000:3000]))

