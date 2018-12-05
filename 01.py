import torch
import numpy

print(torch.__version__)

x=torch.rand(1,10)
print(x)
print(x.sum())
print('==================')
print(x.size)
print(x.size())
print(x.numpy())

y=numpy.array([1,2,3])
print(y)
y=torch.from_numpy(y)
print(y)



x=torch.autograd.Variable(torch.Tensor([3]), requires_grad=True)
y=torch.autograd.Variable(torch.Tensor([5]), requires_grad=True)
z=2*x+y+4
z.backward()
print('dz/dx: {}'.format(x.grad.data))
print('dz/dy: {}'.format(y.grad.data))


class net_name(torch.nn.Module):
    def __init__(self):
        super(net_name, self).__init__()
        self.conv1=torch.nn.Conv2d(3, 10, 3)

    def forward(self, *input):
        out=self.conv1(*input)
        return out

