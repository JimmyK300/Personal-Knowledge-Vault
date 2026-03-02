from one_hidden_mlp import OneHiddenLayerMLP
import numpy as np


def main():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    model = OneHiddenLayerMLP(
        input_dim=2, hidden_dim=4, output_dim=1, lr=0.1, rng_seed=1
    )
    model.fit(X, y, epochs=500, verbose=False)
    preds = model.predict(X)
    print("Preds:", preds.reshape(-1))


if __name__ == "__main__":
    main()
