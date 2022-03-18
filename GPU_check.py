import torch
if torch.cuda.is_available():
    print("Yes")
else:
    print('No')
