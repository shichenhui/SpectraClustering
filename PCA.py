from sklearn.decomposition import PCA
from collections import Counter

data = np.loadtxt(r'C:\Users\panda\Desktop\read_spectra\star_A_F_G_K_2000x4.txt', delimiter=',')
pca = PCA(n_components=30)
data = pca.fit_transform(data)

print(pca.explained_variance_ratio_.sum())