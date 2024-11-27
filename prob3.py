import numpy as np

x = np.array([1, 2, 3, 4, 3, 2, 1, 0])

X = np.fft.fft(x)

print(X)