import numpy as np

from one_hidden_mlp import OneHiddenLayerMLP


class XOR_DATASET:
    @staticmethod
    def xor_inp():
        return np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

    @staticmethod
    def xor_out():
        return np.array([[0], [1], [1], [0]])


# CONSTS and decisions
FEATURE = 2  # feature
OUTPUT = 1  # output
HIDDEN_DIM = 4
EPOCHS = 10000
LEARNING_RATE = 0.1


def main():
    X = XOR_DATASET.xor_inp()
    y = XOR_DATASET.xor_out()

    model = OneHiddenLayerMLP(
        input_dim=FEATURE, hidden_dim=HIDDEN_DIM, output_dim=OUTPUT, lr=LEARNING_RATE
    )
    model.fit(X, y, epochs=EPOCHS, verbose=True)

    print("\nEvaluation:")
    probs = model.predict_proba(X)
    preds = model.predict(X)
    for xi, yi, pi, pr in zip(X, y, probs, preds):
        print("Input:", xi, "Target:", int(yi), "Prob:", float(pi), "Pred:", int(pr))


if __name__ == "__main__":
    main()
