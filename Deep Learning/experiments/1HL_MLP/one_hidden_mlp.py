import numpy as np


class OneHiddenLayerMLP:
    """Simple one-hidden-layer MLP using NumPy.

    API (minimal):
    - fit(X, y, epochs=10000, batch_size=None, verbose=False)
    - predict_proba(X)
    - predict(X, threshold=0.5)
    - get_weights()

    Expects 2D `X` with shape (n_samples, n_features) and `y` with shape
    (n_samples, output_dim) or (n_samples,).
    """

    def __init__(self, input_dim, hidden_dim=4, output_dim=1, lr=0.1, rng_seed=None):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.lr = lr

        self.rng = np.random.default_rng(rng_seed)
        self.W1 = self.rng.normal(0, 0.5, (input_dim, hidden_dim))
        self.W2 = self.rng.normal(0, 0.5, (hidden_dim, output_dim))
        self.b1 = np.zeros((1, hidden_dim))
        self.b2 = np.zeros((1, output_dim))

    # --- activations / helpers ---
    def _relu(self, z):
        return np.maximum(0, z)

    def _d_relu(self, z):
        return (z > 0).astype(int)

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def _calc_loss(self, y, p):
        p = np.clip(p, 1e-15, 1 - 1e-15)
        return -(y * np.log(p) + (1 - y) * np.log(1 - p))

    # --- core operations ---
    def _forward(self, X):
        z1 = X @ self.W1 + self.b1
        a1 = self._relu(z1)
        z2 = a1 @ self.W2 + self.b2
        p = self._sigmoid(z2)
        return p, z1, a1, z2

    def _train_step(self, X, y):
        p, z1, a1, z2 = self._forward(X)
        loss = self._calc_loss(y, p).mean()

        N = X.shape[0]
        d2 = p - y
        dW2 = (a1.T @ d2) / N
        d1 = d2 @ self.W2.T * self._d_relu(z1)
        dW1 = (X.T @ d1) / N
        db1 = np.sum(d1, axis=0, keepdims=True) / N
        db2 = np.sum(d2, axis=0, keepdims=True) / N

        self.W1 -= self.lr * dW1
        self.b1 -= self.lr * db1
        self.W2 -= self.lr * dW2
        self.b2 -= self.lr * db2

        return float(loss)

    # --- public API ---
    def fit(self, X, y, epochs=10000, batch_size=None, verbose=False):
        if X.ndim != 2:
            raise ValueError("X must be 2D with shape (n_samples, n_features)")
        if y.ndim == 1:
            y = y.reshape(-1, 1)
        if X.shape[0] != y.shape[0]:
            raise ValueError("X and y must have the same number of samples")

        loss_history = []
        for i in range(epochs):
            loss = self._train_step(X, y)
            loss_history.append(loss)
            if verbose and i % 1000 == 0:
                print("LOSS AT STEP", i, ":", loss)

        return np.array(loss_history)

    def predict_proba(self, X):
        if X.ndim != 2:
            raise ValueError("X must be 2D with shape (n_samples, n_features)")
        p, *_ = self._forward(X)
        return p

    def predict(self, X, threshold=0.5):
        p = self.predict_proba(X)
        return (p > threshold).astype(int)

    def get_weights(self):
        return {
            "W1": self.W1.copy(),
            "b1": self.b1.copy(),
            "W2": self.W2.copy(),
            "b2": self.b2.copy(),
        }


# Module provides OneHiddenLayerMLP. Demo/training scripts should import the class.
