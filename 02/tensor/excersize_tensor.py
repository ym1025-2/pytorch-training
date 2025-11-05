import numpy as np
import torch

data = np.array([
    [[85, 78], [67, 82], [92, 88], [75, 70], [60, 64]],
    [[70, 68], [77, 72], [85, 90], [60, 65], [78, 76]],
    [[80, 84], [88, 87], [66, 68], [72, 73], [64, 60]]
])

d = torch.from_numpy(data.astype(np.float32)).clone()
print(d)

d_per = torch.permute(d, (2, 0, 1))
print(d_per)

print(torch.sum(d_per, dim = 0))
