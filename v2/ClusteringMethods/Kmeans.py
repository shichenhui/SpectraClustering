# usage:
# python3 file.py data.csv true_class_num setting_class_num pca_num [num_per_class...]
# eg. python3 Kmeans.py index_AFGK_1kx4.csv 4 5 0 1000
# eg. python3 Kmeans.py index_AFGK_1kx4.csv 4 5 0 1000 1000 1000 1000
#

from sklearn.cluster import KMeans
import time, sys
from sklearn.preprocessing import normalize
from collections import Counter
import numpy as np
from sklearn.decomposition import PCA


class Kmeans():

argv = sys.argv
print(argv)
file_name = argv[1]
num_per_class = argv[5:]   # 均衡数据集输一个即可，不均衡数据集输多个
class_num = int(argv[2])
setting_class_num = int(argv[3])
#iter_times = int(argv[5])
pca_num = int(argv[4])

print('load data')
t0 = time.time()
data = np.loadtxt(r'/home/shichenhui/code/spectra_clustering/data/'+file_name, delimiter=',')
t1 = time.time()
print('finished load data, consume time: ', t1-t0)
print('normalize data')
if 'para' in file_name:
    pass
else:
    data = normalize(data)

if pca_num !=0 :
    pca = PCA(n_components=pca_num)
    data = pca.fit_transform(data)
    print(pca.explained_variance_ratio_.sum())

t2 = time.time()
print('finished normalize data, consume time:', t2-t1)


print('run k-means')
y_pred = KMeans(n_clusters=setting_class_num).fit_predict(data)
t3 = time.time()

print('finished run model, consume time', t3-t2)


############################### accuracy #################

if len(num_per_class)==1:
    accu = 0
    n_per = int(num_per_class[0])
    for i in range(class_num):
        r = Counter(y_pred[i*n_per: (i+1)*n_per])
        print(r,r.most_common(1)[0][1]/n_per)
        accu += r.most_common(1)[0][1] / class_num / n_per
    print(accu)

else:
    # num_per_class.append(0)
    accur = []
    point = 0
    for i in range(class_num):
        num_classi = int(num_per_class[i])
        a = y_pred[point:point + num_classi]
        point += num_classi

        # print(num_classi)
        r = Counter(a)
        print(num_classi, r, r.most_common(1)[0][1] / num_classi)

        accu_i = r.most_common(1)[0][1] / num_classi
        accur.append(accu_i)

    print(sum(accur) / class_num)