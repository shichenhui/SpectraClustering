from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import sys
sys.path.append("..")
import time

data = DataLoader.load_spectra_from_csv('../data/spectra_all_proprocessed.csv')

t1 = time.time()
tsne = TSNE(n_components=2,  random_state=0)
result = tsne.fit_transform(data)
t2 = time.time()
print(t2-t1)

label = [1]*1000 + [2]*1000 + [3]*1000

plt.scatter(result[:,0],result[:,1],label)

plt.show()
