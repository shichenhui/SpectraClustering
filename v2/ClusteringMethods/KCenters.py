from matplotlib import pyplot as plt
import numpy as np
import random
from sklearn.datasets import load_iris
from scipy.spatial.distance import cdist
from scipy.spatial.distance import squareform


class KMedoid:
    """
    实现简单的k-medoid算法
    data: 训练数据
    k_num_center: 簇个数

    使用方法：KMediod.run()，返回每个样本的预测类别
    """

    def __init__(self, k_num_center):
        self.k_num_center = k_num_center
        # self.data = data

    def plot_data(self):
        """
        产生测试数据, n_samples表示多少个点, n_features表示几维, centers
        得到的data是n个点各自坐标
        target是每个坐标的分类比如说我规定好四个分类，target长度为n范围为0-3，主要是画图颜色区别
        :return: none
        """

        plt.scatter(self.data[:, 0], self.data[:, 1], )
        # 画图
        plt.show()

    def ou_distance(self):
        print('calc dist_matrix...')
        dist = cdist(self.data, self.data, metric='euclidean')
        # print('squareform')
        # dist = squareform(dist)
        print('finish calc dist_matrix')
        return dist

    def run_k_center(self):
        """
        选定好距离公式开始进行训练
        :param :
        :return:
        """
        print('init ', self.k_num_center, 'centers')
        indexs = list(range(len(self.data)))
        random.shuffle(indexs)  # 随机选择质心
        centers = indexs[:self.k_num_center]

        dist_matrix = self.ou_distance()

        # 确定种类编号
        levels = list(range(self.k_num_center))
        print('start iteration...')
        sample_target = []
        if_stop = False
        times = 0
        while not if_stop:
            times += 1
            print('training step ', times)
            if_stop = True
            classify_points = [[c] for c in centers]
            sample_target = []
            # 遍历数据
            for sample in range(self.data.shape[0]):
                # 计算距离，由距离该数据最近的核心，确定该点所属类别
                distances = [dist_matrix[sample][center] for center in centers]
                cur_level = np.argmin(distances)
                sample_target.append(cur_level)

                # 统计，方便迭代完成后重新计算中间点
                classify_points[cur_level].append(sample)
            # 重新划分质心
            for i in range(self.k_num_center):  # 几类中分别寻找一个最优点
                distances = [dist_matrix[point_1][centers[i]] for point_1 in classify_points[i]]
                now_distances = np.sum(distances)  # 首先计算出现在中心点和其他所有点的距离总和
                for point in classify_points[i]:
                    distances = [dist_matrix[point][point_1] for point_1 in classify_points[i]]
                    new_distance = np.sum(distances)
                    # 计算出该聚簇中各个点与其他所有点的总和，若是有小于当前中心点的距离总和的，中心点去掉
                    if new_distance < now_distances:
                        now_distances = new_distance
                        centers[i] = point  # 换成该点
                        if_stop = False
                        break
        # print('结束')
        return sample_target

    def fit_predict(self, data):
        """
        先获得数据，由传入参数得到杂乱的n个点，然后由这n个点，分为m个类
        :return:
        """
        self.data = np.array(data)
        predict = self.run_k_center()
        return np.array(predict)


if __name__ == '__main__':
    data = load_iris()['data'][:, [0, 2]]
    model = KMediod(data=data, k_num_center=2)
    predict = model.run()  # 运行算法，获取预测标签值

    # 画出结果
    plt.scatter(data[:, 0], data[:, 1], c=predict)
    plt.show()
