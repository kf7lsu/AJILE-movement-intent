import torch
import torch.nn as nn
import torch.nn.functional as f

class neural_model(nn.Module):
    def __init__(self, n_channels):
        super(neural_model, self).__init__()
        #self.bn1 = nn.BatchNorm1d(n_channels, momentum=0.6)
        #self.norm1 = nn.LayerNorm(n_channels)
        #self.act0 = nn.SiLU()
        self.do0 = nn.Dropout()
        self.fc1 = nn.Linear(n_channels, 96)
        self.act1  = nn.ReLU()
        self.do1 = nn.Dropout()
        #self.bn2 = nn.BatchNorm1d(120, momentum=0.6)
        #self.norm2 = nn.GroupNorm(96)
        self.fc2 = nn.Linear(96, 64)
        self.act2  = nn.ReLU()
        #self.do2 = nn.Dropout()
        #self.bn3 = nn.BatchNorm1d(128, momentum=0.6)
        #self.norm3 = nn.LayerNorm(128)
        self.fc3 = nn.Linear(64, 32)
        self.act3  = nn.ReLU()
        #self.do3 = nn.Dropout()
        self.fc4 = nn.Linear(32, 64)
        self.act4  = nn.ReLU()
        #self.do4 = nn.Dropout()
        self.fc5 = nn.Linear(64, 48)
        self.act5  = nn.ReLU()
        self.fc6 = nn.Linear(48, 32)
        self.act6  = nn.ReLU()
        #self.do5 = nn.Dropout()
        #self.bn4 = nn.BatchNorm1d(40, momentum=0.6)
        #self.norm4 = nn.LayerNorm()
        self.fc7 = nn.Linear(32, 1)
        self.act7 = nn.Hardsigmoid(1)
        
    def forward(self, x):
        #x = self.bn1(x)
        #x = self.norm1(x)
        #x = self.act0(x)
        x = self.do0(x)
        x = self.fc1(x)
        x = self.act1(x)
        x = self.do1(x)
        #x = self.bn2(x)
        #x = self.norm2(x)
        x = self.fc2(x)
        x = self.act2(x)
        #x = self.do2(x)
        #x = self.bn3(x)
        #x = self.norm3(x)
        x = self.fc3(x)
        x = self.act3(x)
        #x = self.do3(x)
        x = self.fc4(x)
        x = self.act4(x)
        #x = self.do4(x)
        x = self.fc5(x)
        x = self.act5(x)
        #x = self.do5(x)
        #x = self.bn4(x)
        #x = self.norm4(x)
        x = self.fc6(x)
        x = self.act6(x)
        x = self.fc7(x)
        x = self.act7(x)
        return x
    
if __name__ == "__main__":
    model = neural_model(80)
    inp = torch.tensor(range(80), dtype=torch.float32)
    model.forward(inp)