import torch
import torchvision.datasets as datasets
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable

# 定义超参数
batch_size = 32
learning_rate = 1e-3
num_epoches = 100

# 下载训练集 MNIST 手写数字训练集
train_dataset = datasets.MNIST(root='./data', train=True,
                               transform=transforms.ToTensor(),
                               download=True)

test_dataset = datasets.MNIST(root='./data', train=False,
                              transform=transforms.ToTensor())

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)


class Logstic_Regression(nn.Module):
    def __init__(self, in_dim, n_class):
        super(Logstic_Regression, self).__init__()
        self.logstic = nn.Linear(in_dim, n_class)

    def forward(self, x):
        out = self.logstic(x)
        return out

model = Logstic_Regression(28*28, 10)  # 图片大小是28x28
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate)

for epoch in range(num_epoches):
    print('epoch {}'.format(epoch))
    running_loss = 0.0
    running_acc = 0.0
    for i, data in enumerate(train_loader, 1):
        img, label = data
        img = img.view(img.size(0), -1)  # 将图片展开成 28x28

        img = Variable(img)
        label = Variable(label)

        # 向前传播
        out = model(img)
        loss = criterion(out, label)
        running_loss = loss.item() * label.size(0)
        _, pred = torch.max(out, 1)
        result=(pred == label)
        print(result)
        print(torch.sum(result))
        # num_correct = (pred == label).sum()
    #     running_acc = num_correct.data[0]
    #     # 向后传播
    #     optimizer.zero_grad()
    #     loss.backward()
    #     optimizer.step()
print('ok')