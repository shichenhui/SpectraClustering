from sklearn.cluster import KMeans
from .DPC import DPC

class KMeansDP:
    def __init__(self, n_clusters,data, nn_k):
        self.n_clusters = n_clusters
        self.data = data
        self.dpc = DPC(K=self.n_clusters, nn_k=nn_k)
        self.dpc.data = self.data
        self.centers = self.dpc.search_centers()
        self.kmeans = KMeans(n_clusters=self.n_clusters, init=self.centers)

    def fit_predict(self,data):
        y_pred = self.kmeans.fit_predict(data)
        return y_pred