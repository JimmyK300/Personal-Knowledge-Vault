from tensorflow.keras.datasets import mnist

import numpy as np

from one_hidden_mlp import OneHiddenLayerMLP
from two_hidden_mlp import TwoHiddenLayerMLP

# CONSTS and decisions
FEATURE = 784
OUTPUT = 10
HIDDEN_DIM = 200
EPOCHS = 10
LEARNING_RATE = 0.1
HIDDEN_DIM1 = 200
HIDDEN_DIM2 = 200

# Download and load the data
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)

y_train = np.eye(OUTPUT)[y_train]
y_test  = np.eye(OUTPUT)[y_test]


def main():
    model1 = OneHiddenLayerMLP(
        input_dim=FEATURE, hidden_dim=HIDDEN_DIM, output_dim=OUTPUT, lr=LEARNING_RATE
    )
    model1.fit(x_train, y_train, epochs=EPOCHS, batch_size=100, verbose=True)

    # model2 = TwoHiddenLayerMLP(
    #     input_dim=FEATURE, hidden_dim1=HIDDEN_DIM1, hidden_dim2=HIDDEN_DIM2, output_dim=OUTPUT, lr=LEARNING_RATE
    # )
    # model2.fit(x_train, y_train, epochs=EPOCHS, batch_size=100, verbose=True)
    
    print("\nEvaluation:")
    test_preds1 = model1.predict(x_test)
    test_labels1 = np.argmax(y_test, axis=1)

    accuracy1 = np.mean(test_preds1 == test_labels1)
    print("Test accuracy model 1:", accuracy1)
    # test_preds2 = model2.predict(x_test)
    # test_labels2 = np.argmax(y_test, axis=1)

    # accuracy2 = np.mean(test_preds2 == test_labels2)
    # print("Test accuracy model 2:", accuracy2)


if __name__ == "__main__":
    main()
