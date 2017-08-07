import pandas as pd

import numpy as np

A = np.arange(8).reshape(2,4) + 0.1
B = np.arange(6).reshape(2,3) + 0.2
C= np.arange(12).reshape(3,4) + 0.3

print(A, B, C)

np.hstack([B, A])

print(np.concatenate([B, A], axis=1))
print(np.vstack ([A, C]))
print(np.concatenate([A, C], axis=0))


