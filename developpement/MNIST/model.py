import torch
import torch.nn as nn
import torch.nn.functional as F

class MNISTNet(nn.Module):
    def __init__(self):
        super(MNISTNet, self).__init__()
        self.conv1 = nn.Conv2d(1,8,kernel_size=(5,5))
        self.conv2 = nn.Conv2d(8,16,kernel_size=(5,5))
        self.pool = nn.MaxPool2d(kernel_size=2,stride=2) #divise l'image par 2
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(in_features=16*4*4, out_features = 128)
        self.fc2 = nn.Linear(in_features=128, out_features =64)
        self.fc3 = nn.Linear(in_features=64, out_features =10)

    def forward(self, x):

        x = torch.relu(self.conv1(x))       # First convolution followed by
        x = self.pool(x)                # a relu activation and a max pooling#
        x =torch.relu(self.conv2(x))
        x = self.pool(x)
        x = self.flatten(x)
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x
    
    def get_features(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 4 * 4)
        return x



model=MNISTNet()
print(model)

