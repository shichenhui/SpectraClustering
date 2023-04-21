import minisom
import numpy as np


class SOM:
    def __init__(self, n_clusters, dimensiom, parameters):
        self.n_clusters = n_clusters
        #print(1, n_clusters, dimensiom, self.asymptotic_decay1, )
        self.som = minisom.MiniSom(1, n_clusters, dimensiom, decay_function=self.asymptotic_decay1, **parameters)
        pass

    def asymptotic_decay1(self, learning_rate, t, max_iter):
        """Decay function of the learning process.
        Parameters
        ----------
        learning_rate : float
            current learning rate.

        t : int
            current iteration.

        max_iter : int
            maximum number of iterations for the training.
        """
        return learning_rate / (1 + t / (max_iter / 15))

    def fit_predict(self, data):
        self.som.random_weights_init(data)
        self.som.train(data, 200, random_order=True, verbose=False)
        w_x, y_pred = zip(*[self.som.winner(d) for d in data])
        w_x = np.array(w_x)
        y_pred = np.array(y_pred)
        return y_pred