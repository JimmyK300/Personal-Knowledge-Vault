import numpy as np

from one_hidden_mlp import OneHiddenLayerMLP


# CONSTS and decisions
FEATURE = 2  # feature
OUTPUT = 1  # output
HIDDEN_DIM = 500
EPOCHS = 100000
LEARNING_RATE = 0.1

rng = np.random.default_rng(42)

# --- Training set (20 samples) ---
X_train = rng.uniform(-1, 1, size=(500, FEATURE))
y_train = (X_train[:, 0] * X_train[:, 1] > 0).astype(int).reshape(-1, 1)

# flip 100 random labels
noise_count = 100
noise_idx = rng.choice(len(y_train), size=noise_count, replace=False)

y_train[noise_idx] = 1 - y_train[noise_idx]

# --- Test set (1000 samples) ---
X_test = rng.uniform(-1, 1, size=(1000, 2))
y_test = (X_test[:, 0] * X_test[:, 1] > 0).astype(int).reshape(-1, 1)

def main():
    X = X_train
    y = y_train

    model = OneHiddenLayerMLP(
        input_dim=FEATURE, hidden_dim=HIDDEN_DIM, output_dim=OUTPUT, lr=LEARNING_RATE
    )
    for I in range(200):
        model.fit(X, y, epochs=500)

        # print("\nEvaluation:")
        # probs = model.predict_proba(X_test)
        # preds = model.predict(X_test)
        # for xi, yi, pi, pr in zip(X_test, y_test, probs, preds):
        #     print("Input:", xi, "Target:", int(yi), "Prob:", float(pi), "Pred:", int(pr))
        
        test_loss = model.compute_loss(X_test, y_test)
        train_loss = model.compute_loss(X_train, y_train)

        print(f"Block {I+1} | Train loss: {train_loss:.4f} | Test loss: {test_loss:.4f}")
        # print("Train loss:", train_loss)
        # print("Test loss:", test_loss)
    


if __name__ == "__main__":
    main()
