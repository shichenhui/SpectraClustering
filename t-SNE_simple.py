
import numpy as np
import matplotlib.pyplot as plt


# 输入为(n*m)的矩阵，表示n个样本，m个属性
# 返回一个距离矩阵
def cal_pairwise_dist(x):
    # '''计算pairwise 距离, x是matrix
    # (a-b)^2 = a^2 + b^2 - 2*a*b
    # '''
    sum_x = np.sum(np.square(x), 1)
    # print -2 * np.dot(x, x.T)
    # print np.add(-2 * np.dot(x, x.T), sum_x).T
    dist = np.add(np.add(-2 * np.dot(x, x.T), sum_x).T, sum_x)
    # 返回任意两个点之间距离的平方
    return dist


# 计算困惑度，最终会选择合适的beta，也就是每个点的方差啦
def cal_perplexity(dist, idx=0, beta=1.0):
    # '''计算perplexity, D是距离向量，
    # idx指dist中自己与自己距离的位置，beta是高斯分布参数
    # 这里的perp仅计算了熵，方便计算
    # '''
    prob = np.exp(-dist * beta)
    # 设置自身prob为0
    prob[idx] = 0
    sum_prob = np.sum(prob)
    if sum_prob == 0:
        prob = np.maximum(prob, 1e-12)
        perp = -12
    else:
        prob /= sum_prob
        perp = 0
        for pj in prob:
            if pj != 0:
                perp += -pj * np.log(pj)
    # 困惑度和pi\j的概率分布
    return perp, prob


def seach_prob(x, tol=1e-5, perplexity=30.0):
    # '''二分搜索寻找beta,并计算pairwise的prob
    # '''
    # 初始化参数
    print("Computing pairwise distances...")
    (n, d) = x.shape
    dist = cal_pairwise_dist(x)
    pair_prob = np.zeros((n, n))
    beta = np.ones((n, 1))
    # 取log，方便后续计算
    base_perp = np.log(perplexity)

    for i in range(n):
        if i % 500 == 0:
            print("Computing pair_prob for point %s of %s ..." % (i, n))

        betamin = -np.inf
        betamax = np.inf
        # dist[i]需要换不能是所有点
        perp, this_prob = cal_perplexity(dist[i], i, beta[i])

        # 二分搜索,寻找最佳sigma下的prob
        perp_diff = perp - base_perp
        tries = 0
        while np.abs(perp_diff) > tol and tries < 50:
            if perp_diff > 0:
                betamin = beta[i].copy()
                if betamax == np.inf or betamax == -np.inf:
                    beta[i] = beta[i] * 2
                else:
                    beta[i] = (beta[i] + betamax) / 2
            else:
                betamax = beta[i].copy()
                if betamin == np.inf or betamin == -np.inf:
                    beta[i] = beta[i] / 2
                else:
                    beta[i] = (beta[i] + betamin) / 2

            # 更新perb,prob值
            perp, this_prob = cal_perplexity(dist[i], i, beta[i])
            perp_diff = perp - base_perp
            tries = tries + 1
        # 记录prob值
        pair_prob[i,] = this_prob
    print("Mean value of sigma: ", np.mean(np.sqrt(1 / beta)))
    # 每个点对其他点的条件概率分布pi\j
    return pair_prob


def tsne(x, no_dims=2, initial_dims=50, perplexity=30.0, max_iter=800):
    """Runs t-SNE on the dataset in the NxD array x
    to reduce its dimensionality to no_dims dimensions.
    The syntaxis of the function is Y = tsne.tsne(x, no_dims, perplexity),
    where x is an NxD NumPy array.
    """

    # Check inputs
    if isinstance(no_dims, float):
        print("Error: array x should have type float.")
        return -1
    if round(no_dims) != no_dims:
        print("Error: number of dimensions should be an integer.")
        return -1

    (n, d) = x.shape
    print(x.shape)

    # 动量
    eta = 500
    # 随机初始化Y
    y = np.random.randn(n, no_dims)
    # dy梯度
    dy = np.zeros((n, no_dims))
    # 对称化
    P = seach_prob(x, 1e-5, perplexity)
    P = P + np.transpose(P)
    P = P / np.sum(P)  # pij
    # early exaggeration
    # pi\j
    P = P * 4
    P = np.maximum(P, 1e-12)

    # Run iterations
    for iter in range(max_iter):
        # Compute pairwise affinities
        sum_y = np.sum(np.square(y), 1)
        num = 1 / (1 + np.add(np.add(-2 * np.dot(y, y.T), sum_y).T, sum_y))
        num[range(n), range(n)] = 0
        Q = num / np.sum(num)  # qij
        Q = np.maximum(Q, 1e-12)  # X与Y逐位比较取其大者

        # Compute gradient
        # pij-qij
        PQ = P - Q
        # 梯度dy
        for i in range(n):
            dy[i, :] = np.sum(np.tile(PQ[:, i] * num[:, i], (no_dims, 1)).T * (y[i, :] - y), 0)

        # 更新y
        y = y - eta * dy

        # 减去均值
        y = y - np.tile(np.mean(y, 0), (n, 1))
        # Compute current value of cost function
        if (iter + 1) % 50 == 0:
            if iter > 100:
                C = np.sum(P * np.log(P / Q))
            else:
                C = np.sum(P / 4 * np.log(P / 4 / Q))
            print("Iteration ", (iter + 1), ": error is ", C)
        # Stop lying about P-values
        if iter == 100:
            P = P / 4
    print("finished training!")
    return y


if __name__ == "__main__":
    print("Run Y = tsne.tsne(X, no_dims, perplexity) to perform t-SNE on your dataset.")
    print("Running example on 2,500 MNIST digits...")
    X = np.loadtxt("mnist2500_X.txt")
    labels = np.loadtxt("mnist2500_labels.txt")
    Y = tsne(X, 2, 50, 20.0)
    plt.scatter(Y[:, 0], Y[:, 1], 20, labels)
    plt.show()