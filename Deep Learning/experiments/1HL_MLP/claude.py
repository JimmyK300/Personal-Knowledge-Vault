"""
MNIST Digit Classifier
======================
Two implementations:
  1. NumPy-only MLP (runs anywhere, ~97% accuracy)
  2. PyTorch CNN (run if you have PyTorch, ~99%+ accuracy)

Usage:
  python mnist_classifier.py            # auto-detects PyTorch, falls back to NumPy
  python mnist_classifier.py --numpy    # force NumPy version
  python mnist_classifier.py --torch    # force PyTorch version
"""

import sys
import numpy as np

# ─────────────────────────────────────────────
# NUMPY MLP IMPLEMENTATION
# ─────────────────────────────────────────────

def load_mnist_numpy():
    """Load MNIST via keras (if available) or generate toy data for demo."""
    try:
        from tensorflow.keras.datasets import mnist
        (X_train, y_train), (X_test, y_test) = mnist.load_data()
        X_train = X_train.reshape(-1, 784).astype(np.float32) / 255.0
        X_test  = X_test.reshape(-1, 784).astype(np.float32) / 255.0
        print("Loaded MNIST via Keras.")
        return X_train, y_train, X_test, y_test
    except ImportError:
        pass

    try:
        import urllib.request, gzip, os, struct
        base = "https://storage.googleapis.com/cvdf-datasets/mnist/"
        files = {
            "train_images": "train-images-idx3-ubyte.gz",
            "train_labels": "train-labels-idx1-ubyte.gz",
            "test_images":  "t10k-images-idx3-ubyte.gz",
            "test_labels":  "t10k-labels-idx1-ubyte.gz",
        }
        os.makedirs("mnist_data", exist_ok=True)
        def download(name):
            path = f"mnist_data/{files[name]}"
            if not os.path.exists(path):
                print(f"Downloading {files[name]}...")
                urllib.request.urlretrieve(base + files[name], path)
            return path

        def read_images(path):
            with gzip.open(path, 'rb') as f:
                _, n, r, c = struct.unpack('>IIII', f.read(16))
                return np.frombuffer(f.read(), np.uint8).reshape(n, r*c).astype(np.float32) / 255.0

        def read_labels(path):
            with gzip.open(path, 'rb') as f:
                struct.unpack('>II', f.read(8))
                return np.frombuffer(f.read(), np.uint8)

        X_train = read_images(download("train_images"))
        y_train = read_labels(download("train_labels"))
        X_test  = read_images(download("test_images"))
        y_test  = read_labels(download("test_labels"))
        print("Downloaded and loaded MNIST.")
        return X_train, y_train, X_test, y_test
    except Exception as e:
        print(f"Could not download MNIST ({e}). Using random demo data (accuracy won't be meaningful).")
        X_train = np.random.randn(1000, 784).astype(np.float32)
        y_train = np.random.randint(0, 10, 1000)
        X_test  = np.random.randn(200, 784).astype(np.float32)
        y_test  = np.random.randint(0, 10, 200)
        return X_train, y_train, X_test, y_test


class NumpyMLP:
    """
    3-layer MLP: 784 → 256 → 128 → 10
    Activations: ReLU (hidden), Softmax (output)
    Optimizer: Mini-batch SGD with momentum
    Regularization: L2 weight decay + Dropout
    """

    def __init__(self, layer_sizes=(784, 256, 128, 10), lr=0.01, momentum=0.9,
                 weight_decay=1e-4, dropout_rate=0.2):
        self.lr = lr
        self.mu = momentum
        self.wd = weight_decay
        self.dropout_rate = dropout_rate

        # He initialization
        self.W, self.b, self.vW, self.vb = [], [], [], []
        for i in range(len(layer_sizes) - 1):
            fan_in = layer_sizes[i]
            W = np.random.randn(layer_sizes[i], layer_sizes[i+1]).astype(np.float32) * np.sqrt(2.0 / fan_in)
            b = np.zeros(layer_sizes[i+1], dtype=np.float32)
            self.W.append(W); self.b.append(b)
            self.vW.append(np.zeros_like(W)); self.vb.append(np.zeros_like(b))

    def relu(self, x):       return np.maximum(0, x)
    def relu_grad(self, x):  return (x > 0).astype(np.float32)

    def softmax(self, x):
        e = np.exp(x - x.max(axis=1, keepdims=True))
        return e / e.sum(axis=1, keepdims=True)

    def forward(self, X, training=True):
        self.cache = {'A': [X]}
        A = X
        for i, (W, b) in enumerate(zip(self.W, self.b)):
            Z = A @ W + b
            if i < len(self.W) - 1:
                A = self.relu(Z)
                if training and self.dropout_rate > 0:
                    mask = (np.random.rand(*A.shape) > self.dropout_rate).astype(np.float32)
                    A *= mask / (1 - self.dropout_rate)
                    self.cache[f'mask_{i}'] = mask
            else:
                A = self.softmax(Z)
            self.cache['A'].append(A)
            self.cache[f'Z_{i}'] = Z
        return A

    def loss(self, probs, y):
        n = len(y)
        log_p = -np.log(probs[np.arange(n), y] + 1e-9)
        l2 = sum((W**2).sum() for W in self.W)
        return log_p.mean() + 0.5 * self.wd * l2

    def backward(self, y):
        n = len(y)
        dA = self.cache['A'][-1].copy()
        dA[np.arange(n), y] -= 1
        dA /= n

        for i in reversed(range(len(self.W))):
            A_prev = self.cache['A'][i]
            dW = A_prev.T @ dA + self.wd * self.W[i]
            db = dA.sum(axis=0)

            # SGD with momentum
            self.vW[i] = self.mu * self.vW[i] - self.lr * dW
            self.vb[i] = self.mu * self.vb[i] - self.lr * db
            self.W[i] += self.vW[i]
            self.b[i]  += self.vb[i]

            if i > 0:
                dA = dA @ self.W[i].T * self.relu_grad(self.cache[f'Z_{i-1}'])
                if f'mask_{i-1}' in self.cache:
                    dA *= self.cache[f'mask_{i-1}'] / (1 - self.dropout_rate)

    def predict(self, X):
        probs = self.forward(X, training=False)
        return probs.argmax(axis=1)

    def accuracy(self, X, y):
        return (self.predict(X) == y).mean()

    def fit(self, X, y, X_val, y_val, epochs=20, batch_size=128):
        n = len(X)
        print(f"\n{'─'*55}")
        print(f"  NumPy MLP | layers: 784→256→128→10 | lr={self.lr}")
        print(f"{'─'*55}")
        print(f"  {'Epoch':>5}  {'Loss':>8}  {'Train Acc':>10}  {'Val Acc':>10}")
        print(f"{'─'*55}")

        best_val, best_weights = 0, None

        for epoch in range(1, epochs + 1):
            # Learning rate decay
            if epoch in (10, 15):
                self.lr *= 0.5

            idx = np.random.permutation(n)
            X_shuf, y_shuf = X[idx], y[idx]
            total_loss = 0

            for start in range(0, n, batch_size):
                Xb = X_shuf[start:start+batch_size]
                yb = y_shuf[start:start+batch_size]
                probs = self.forward(Xb, training=True)
                total_loss += self.loss(probs, yb) * len(yb)
                self.backward(yb)

            avg_loss  = total_loss / n
            train_acc = self.accuracy(X, y)
            val_acc   = self.accuracy(X_val, y_val)

            print(f"  {epoch:>5}  {avg_loss:>8.4f}  {train_acc:>9.2%}  {val_acc:>9.2%}")

            if val_acc > best_val:
                best_val = val_acc
                best_weights = [(W.copy(), b.copy()) for W, b in zip(self.W, self.b)]

        # Restore best weights
        if best_weights:
            for i, (W, b) in enumerate(best_weights):
                self.W[i], self.b[i] = W, b

        print(f"{'─'*55}")
        print(f"  Best validation accuracy: {best_val:.2%}")
        print(f"{'─'*55}\n")


def run_numpy():
    np.random.seed(42)
    X_train, y_train, X_test, y_test = load_mnist_numpy()

    model = NumpyMLP(
        layer_sizes=(784, 256, 128, 10),
        lr=0.05,
        momentum=0.9,
        weight_decay=1e-4,
        dropout_rate=0.2
    )
    model.fit(X_train, y_train, X_test, y_test, epochs=20, batch_size=256)

    test_acc = model.accuracy(X_test, y_test)
    print(f"Final Test Accuracy: {test_acc:.2%}")

    # Per-class accuracy
    print("\nPer-digit accuracy:")
    for digit in range(10):
        mask = y_test == digit
        acc = model.accuracy(X_test[mask], y_test[mask])
        bar = '█' * int(acc * 20)
        print(f"  {digit}: {bar:<20} {acc:.1%}")

    return model


# ─────────────────────────────────────────────
# PYTORCH CNN IMPLEMENTATION
# ─────────────────────────────────────────────

def run_pytorch():
    import torch
    import torch.nn as nn
    import torch.optim as optim
    from torch.utils.data import DataLoader
    from torchvision import datasets, transforms

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # Data loading with augmentation
    train_transform = transforms.Compose([
        transforms.RandomAffine(degrees=10, translate=(0.1, 0.1), scale=(0.9, 1.1)),
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    test_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])

    train_data = datasets.MNIST(root='./data', train=True,  download=True, transform=train_transform)
    test_data  = datasets.MNIST(root='./data', train=False, download=True, transform=test_transform)

    train_loader = DataLoader(train_data, batch_size=128, shuffle=True,  num_workers=2)
    test_loader  = DataLoader(test_data,  batch_size=256, shuffle=False, num_workers=2)

    # CNN Architecture
    class MnistCNN(nn.Module):
        """
        Conv block 1: 1→32 channels, 3×3, ReLU, BatchNorm, MaxPool
        Conv block 2: 32→64 channels, 3×3, ReLU, BatchNorm, MaxPool
        Conv block 3: 64→128 channels, 3×3, ReLU, BatchNorm
        FC: 128*3*3 → 256 → 10
        """
        def __init__(self):
            super().__init__()
            self.features = nn.Sequential(
                # Block 1
                nn.Conv2d(1, 32, 3, padding=1),
                nn.BatchNorm2d(32),
                nn.ReLU(inplace=True),
                nn.Conv2d(32, 32, 3, padding=1),
                nn.BatchNorm2d(32),
                nn.ReLU(inplace=True),
                nn.MaxPool2d(2, 2),       # 28x28 → 14x14
                nn.Dropout2d(0.1),

                # Block 2
                nn.Conv2d(32, 64, 3, padding=1),
                nn.BatchNorm2d(64),
                nn.ReLU(inplace=True),
                nn.Conv2d(64, 64, 3, padding=1),
                nn.BatchNorm2d(64),
                nn.ReLU(inplace=True),
                nn.MaxPool2d(2, 2),       # 14x14 → 7x7
                nn.Dropout2d(0.1),

                # Block 3
                nn.Conv2d(64, 128, 3, padding=1),
                nn.BatchNorm2d(128),
                nn.ReLU(inplace=True),
            )
            self.classifier = nn.Sequential(
                nn.Flatten(),
                nn.Linear(128 * 7 * 7, 256),
                nn.ReLU(inplace=True),
                nn.Dropout(0.4),
                nn.Linear(256, 10)
            )

        def forward(self, x):
            return self.classifier(self.features(x))

    model = MnistCNN().to(device)
    total_params = sum(p.numel() for p in model.parameters())
    print(f"\nModel parameters: {total_params:,}")

    optimizer = optim.Adam(model.parameters(), lr=1e-3, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=15)
    criterion = nn.CrossEntropyLoss()

    print(f"\n{'─'*55}")
    print(f"  PyTorch CNN | {'Epoch':>5}  {'Loss':>8}  {'Train':>7}  {'Test':>7}")
    print(f"{'─'*55}")

    for epoch in range(1, 16):
        # Train
        model.train()
        total_loss, correct, total = 0, 0, 0
        for X, y in train_loader:
            X, y = X.to(device), y.to(device)
            optimizer.zero_grad()
            out = model(X)
            loss = criterion(out, y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * len(y)
            correct += (out.argmax(1) == y).sum().item()
            total += len(y)
        scheduler.step()

        # Evaluate
        model.eval()
        test_correct, test_total = 0, 0
        with torch.no_grad():
            for X, y in test_loader:
                X, y = X.to(device), y.to(device)
                out = model(X)
                test_correct += (out.argmax(1) == y).sum().item()
                test_total += len(y)

        train_acc = correct / total
        test_acc  = test_correct / test_total
        avg_loss  = total_loss / total
        print(f"  {epoch:>5}  {avg_loss:>8.4f}  {train_acc:>6.2%}  {test_acc:>6.2%}")

    print(f"{'─'*55}")
    print(f"  Final Test Accuracy: {test_acc:.2%}")
    print(f"{'─'*55}")

    # Save model
    torch.save(model.state_dict(), "mnist_cnn.pth")
    print("\nModel saved to mnist_cnn.pth")
    print("To reload: model.load_state_dict(torch.load('mnist_cnn.pth'))")

    return model


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    use_torch  = "--torch" in sys.argv
    use_numpy  = "--numpy" in sys.argv

    if use_numpy:
        run_numpy()
    elif use_torch:
        run_pytorch()
    else:
        try:
            import torch
            print("PyTorch detected — running CNN version.")
            print("(Use --numpy to force the NumPy version)\n")
            run_pytorch()
        except ImportError:
            print("PyTorch not found — running NumPy MLP version.")
            print("(Install PyTorch for the CNN version with ~99% accuracy)\n")
            run_numpy()