import torch
import torch.nn as nn
import torch.optim as optim

from torch.utils.data import DataLoader
from torch.utils.data import Subset
from torchvision import datasets, transforms

transform = transforms.ToTensor()

train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST(root='./data', train=False, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=100, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=100)

class MLP(nn.Module):
    def __init__(self, input_dim=784, hidden_dim=200, output_dim=10):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

class DeepMLP(nn.Module):
    def __init__(self, input_dim=784, hidden_dim=200, depth=8, output_dim=10):
        super().__init__()
        
        layers = []
        layers.append(nn.Linear(input_dim, hidden_dim))
        layers.append(nn.BatchNorm1d(hidden_dim))
        layers.append(nn.ReLU())
        
        for _ in range(depth - 1):
            layers.append(nn.Linear(hidden_dim, hidden_dim))
            layers.append(nn.BatchNorm1d(hidden_dim))
            layers.append(nn.ReLU())
        
        layers.append(nn.Linear(hidden_dim, output_dim))
        
        self.net = nn.Sequential(*layers)

    def forward(self, x):
        return self.net(x)

class ResidualBlock(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.fc = nn.Linear(dim, dim)
        self.bn = nn.BatchNorm1d(dim)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.fc(x)
        out = self.bn(out)
        out = self.relu(out)
        return x + out

class ResMLP(nn.Module):
    def __init__(self, input_dim=784, hidden_dim=200, depth=8, output_dim=10):
        super().__init__()
        
        self.input = nn.Linear(input_dim, hidden_dim)
        self.blocks = nn.Sequential(
            *[ResidualBlock(hidden_dim) for _ in range(depth)]
        )
        self.output = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = self.input(x)
        x = torch.relu(x)
        x = self.blocks(x)
        x = self.output(x)
        return x

def evaluate(loader):
    model.eval()
    correct = 0
    total = 0
    
    with torch.no_grad():
        for images, labels in loader:
            images = images.view(images.size(0), -1)
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    
    return correct / total

for hi in [12]:
    model = ResMLP(depth=hi)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.1)
    
    train_acc = []
    
    for epoch in range(10):
        model.train()
        total_loss = 0
        total = 0
        correct = 0
        for images, labels in train_loader:
            images = images.view(images.size(0), -1)

            optimizer.zero_grad()        # clear old gradients
            outputs = model(images)      # forward
            loss = criterion(outputs, labels)
            loss.backward()              # compute gradients
            optimizer.step()             # update weights
            
            _, predicted = torch.max(outputs, 1)
            
            total_loss += loss.item()
            
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
        train_acc.append(correct / total)
        
        print(f"Epoch {epoch}: loss = {total_loss:.4f}")
    print("L bn resdiual:", hi)
    print("Train accuracy:", train_acc[-1])
    print("Test accuracy:", evaluate(test_loader))
    print("Epoch to conv:",  train_acc)