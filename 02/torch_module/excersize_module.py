import torch
from torch import nn

class MyModel(nn.Module):

    def __init__(self, mytensor: torch.tensor, elem_add = float, elem_multiply = float):
        super().__init__()
        self.mytensor = torch.ones([2, 3])
        self.elem_add = elem_add
        self.elem_multiply = elem_multiply

    def foward(self, tensor):
        tensor = torch.add(tensor, self.mytensor)
        tensor = torch.add(tensor, self.elem_add)
        tensor - torch.matmul(tensor. self.elem_multiply)

        return tensor

if __name__ == "__main__":
    myModel = MyModel(3, 2.0)
    _input = torch.ones([2, 3])

    out1 = myModel(_input)
    out2 = myModel.forward(_input)

    print(out1)
    print(out2)