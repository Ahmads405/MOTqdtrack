# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import torch
print(torch.cuda.is_available())
print(torch.version.cuda)
print(torch.__version__)
torch.cuda.empty_cache()
# to get cuda nvidia-smi