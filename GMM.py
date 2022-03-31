from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
import numpy as np
def generate_data(mean, cov, nums):
    plt.axis("equal")
    X = []
    Y = None
    for i in range(len(mean)):
        X.append(np.random.multivariate_normal(mean[i], np.diag(cov[i]), nums[i]))
        plt.scatter(X[i][:, 0], X[i][:, 1])

    plt.show()
    X = np.array(X)
    X=X.reshape((X.shape[0]*X.shape[1],X.shape[2]))

    return X
    
X = generate_data([[-2, 0],[10,10],[5,5]], [[1,10],[1,2],[2,2]], [100,100,100])

gmmModel = GaussianMixture(n_components=3, covariance_type='full')

gmmModel.fit(X)

print(gmmModel.converged_)
