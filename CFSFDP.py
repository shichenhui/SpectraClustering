import numpy as np
import matplotlib.pyplot as plt
import time

class DPC:
    """

    :param data: 数据
    :param nn_k: 近邻数
    :param K: 簇数

    使用方法，调用run() 方法运行算法，返回预测类别标签
    """
    def __init__(self, data, nn_k, K):
        self.data = np.array(data)
        self.nn_k = nn_k
        self.K = K
        self.dist_matrix = self.calc_dist_matrix()
        self.density = None
        self.density_sort_index = self.calc_density()

    def calc_dist_matrix(self):
        # 计算距离矩阵
        n = self.data.shape[0]
        dist = np.zeros((n,n))
        for i in range(n):
            for j in range(i + 1, n):
                dist[i, j] = np.linalg.norm(self.data[i,:] - self.data[j,:])
                dist[j, i] = dist[i, j]
        return dist

    def calc_density(self):
        # 计算每个点的密度
        dist_sorted = np.sort(self.dist_matrix, axis=1)    # 将距离矩阵按行排序
        knn_dist = dist_sorted[:,1:self.nn_k+1]     #
        dist_c = knn_dist.sum() / knn_dist.size / 2  # 截断半径，没有规定的方法
        density = []
        for i in dist_sorted:
            density.append(i[i<dist_c].size)  # 与此点距离小于截断半径的点个数
        self.density = np.array(density)
        density_sort_index = np.argsort(self.density)[::-1]  # 按密度降序排序，返回排序后的索引
        return density_sort_index

    def calc_delta(self):
        # 计算delta，需要用到
        deltas = np.zeros(self.data.shape[0])
        # 先给密度最大的点设定delta
        deltas[self.density_sort_index[0]] = self.dist_matrix[self.density_sort_index[0]].max()

        # 给每个点设定delta，取值为密度大于此点的点，到此点的距离的最小值
        for i in range(1, self.density_sort_index.size):
            delta_i = np.min(self.dist_matrix[self.density_sort_index[i]][self.density_sort_index[0:i]])
            deltas[self.density_sort_index[i]] = delta_i

        return deltas

    def secrch_DP(self):
        # 算法执行函数，返回每个点的密度和delta值
        deltas = self.calc_delta()
        return self.density, np.array(deltas)

    def run(self):
        n = self.data.shape[0]
        density, delta = self.secrch_DP()
        factor = density*delta
        centers = np.argsort(factor)[::-1][:self.K]
        labels = np.full(n, -1)
        for i in range(self.K):
            labels[centers[i]] = i

        dist_index = np.argsort(self.dist_matrix, axis=1)

        for i in self.density_sort_index:
            for j in range(1, n):
                if density[i] <= density[dist_index[i, j]] and labels[dist_index[i, j]] != -1 and i not in centers:
                    labels[i] = labels[dist_index[i, j]]
                    break

        return labels

if __name__ == '__main__':
    from sklearn.datasets import load_iris

    data = load_iris()['data'][:,[0,3]]
    data = data * 5 + np.random.rand(data.shape[0], data.shape[1])
    data = np.append(data,np.array([[40,2]]),axis=0)
    print(data.shape)

    t1 = time.time()
    model = DPC(data, nn_k=8, K = 2)
    density, deltas = model.secrch_DP()
    label = model.run()
    t2 = time.time()
    print('running time: ',t2-t1)

    plt.scatter(data[:,0], data[:,1], c=model.density)
    plt.show()
    plt.scatter(data[:,0], data[:,1], c=deltas)
    plt.show()
    plt.scatter(model.density, deltas)
    plt.show()

    plt.scatter(data[:,0], data[:,1], c=label)
    plt.show()
    # print(label)