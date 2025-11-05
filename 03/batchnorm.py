import torch
from torch import nn

if __name__ == "__main__":
    _in = torch.ones(32, 1024)
    print(f"_in: {_in.shape}")

    fc1 = nn.Linear(in_features=1024, out_features=256, bias = True)
    out1 = fc1(_in)
    print(f"fc1: {out1.shape}")

    fc2 = nn.Linear(in_features=1024, out_features=2048, bias = True)
    out2 = fc2(_in)
    print(f"fc2: {out2.shape}")

    out3 = torch.reshape(out1, (32, 16, 16))
    print(f"fc3: {out3.shape}")