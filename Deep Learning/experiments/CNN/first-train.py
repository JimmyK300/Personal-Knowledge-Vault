import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import os
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().with_name("mnist_cnn_simple.pth")

# -----------------------------
# 1. Device
# -----------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# -----------------------------
# 2. Dataset
# -----------------------------
transform = transforms.ToTensor()

train_dataset = datasets.MNIST(
    root="./data",
    train=True,
    download=True,
    transform=transform
)

test_dataset = datasets.MNIST(
    root="./data",
    train=False,
    download=True,
    transform=transform
)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64)

# -----------------------------
# 3. Model
# -----------------------------

model = nn.Sequential(
    nn.Conv2d(1, 8, 3, padding=1),   # (1,28,28) -> (8,28,28)
    nn.ReLU(),
    nn.MaxPool2d(2),                 # -> (8,14,14)

    nn.Conv2d(8, 16, 3, padding=1),  # -> (16,14,14)
    nn.ReLU(),
    nn.MaxPool2d(2),                 # -> (16,7,7)

    nn.Flatten(),
    nn.Linear(16 * 7 * 7, 10)
).to(device)
# 1. Loading Logic (Place before training loop)
if os.path.exists(MODEL_PATH):
    checkpoint = torch.load(MODEL_PATH, map_location=device, weights_only=True)
    try:
        model.load_state_dict(checkpoint)
    except RuntimeError as exc:
        raise RuntimeError(
            f"Checkpoint at {MODEL_PATH} does not match this script's simple CNN architecture. "
            "Use the matching model definition or delete this checkpoint so the script can retrain."
        ) from exc
    print(f"Loaded existing model from {MODEL_PATH}. Skipping training.")
else:
    print("No saved model found. Starting training...")
    # -----------------------------
    # 4. Loss + Optimizer
    # -----------------------------
    loss_fn = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-2)

    # -----------------------------
    # 5. Training loop
    # -----------------------------
    epochs = 10

    for epoch in range(epochs):

        model.train()
        total_loss = 0

        for x, y in train_loader:

            x, y = x.to(device), y.to(device)

            pred = model(x)
            loss = loss_fn(pred, y)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        print(f"Epoch {epoch+1} | loss: {total_loss/len(train_loader):.4f}")
    # 2. Saving Logic (Place after training loop completes)
    torch.save(model.state_dict(), MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}.")


# -----------------------------
# 6. Evaluation
# -----------------------------
model.eval()

correct = 0
total = 0

with torch.no_grad():
    for x, y in test_loader:

        x, y = x.to(device), y.to(device)

        pred = model(x)
        predicted = pred.argmax(dim=1)

        correct += (predicted == y).sum().item()
        total += y.size(0)

accuracy = correct / total
print("Test accuracy:", accuracy)


# # -----------------------------
# # 7. Feature map visualization
# # -----------------------------

# # get one test image
# x, label = test_dataset[1]

# x = x.unsqueeze(0).to(device)   # add batch dimension

# conv1 = model[0]
# conv2 = model[3]

# with torch.no_grad():
#     features1 = conv1(x)        # (1,8,28,28)
#     features2 = conv2(features1) # (1,16,28,28)

# # -----------------------------
# # show input + conv1 maps
# # -----------------------------
# fig, axes = plt.subplots(1, 9, figsize=(15,3))

# axes[0].imshow(x[0,0].cpu(), cmap="gray")
# axes[0].set_title("input")
# axes[0].axis("off")

# for i in range(8):
#     axes[i+1].imshow(features1[0,i].cpu(), cmap="gray")
#     axes[i+1].set_title(f"f{i}")
#     axes[i+1].axis("off")

# plt.show()

# # -----------------------------
# # show conv2 maps
# # -----------------------------
# fig, axes = plt.subplots(4,4, figsize=(6,6))

# for i in range(16):

#     r = i // 4
#     c = i % 4

#     axes[r,c].imshow(features2[0,i].cpu(), cmap="gray")
#     axes[r,c].set_title(f"f{i}")
#     axes[r,c].axis("off")

# plt.show()





# 1. Grab a single test image
x, y = next(iter(test_loader))
single_image = x[0:1].to(device)  # Keep batch dimension: shape (1, 1, 28, 28)

model.eval()
with torch.no_grad():
    first_conv = model[0]
    feature_maps = first_conv(single_image)

# 3. Convert to NumPy for plotting
# feature_maps shape: (1, num_filters, H_out, W_out)
# Squeeze out the batch dimension to get (num_filters, H_out, W_out)
activations = feature_maps.squeeze(0).cpu().numpy()

# 4. Plot the feature maps
num_filters = activations.shape[0]
fig, axes = plt.subplots(1, num_filters, figsize=(15, 3))

# Handle case where there's only 1 filter to prevent indexing errors
if num_filters == 1:
    axes = [axes]

for i in range(num_filters):
    axes[i].imshow(activations[i], cmap='gray')
    axes[i].set_title(f"Filter {i+1}")
    axes[i].axis('off')

plt.suptitle(f"Layer 1 Feature Maps for Label: {y[0].item()}")
plt.tight_layout()
plt.show()