import numpy as np
from scipy.signal import residue

def H(z):
    return (1+0.3*pow(z, -1)+0.1*pow(z, -2))/(1-0.2*pow(z, -1)-0.1*pow(z, -2))

def inverse_z_transform(b, a, N):
    r, p, k = residue(b, a)
    h = np.zeros(N)
    for n in range(N):
        h[n] = sum(r[i] * (p[i] ** n) for i in range(len(r)))
    return h

z = np.exp(1j * 2 * np.pi / 10)

hz = H(z)

r_part = hz.real
i_part = hz.imag

print(np.abs(hz))
print(np.arctan(i_part/r_part))

b = [1, 0.3, 0.1]
a = [1, -0.2, -0.1]
N = 7

h = inverse_z_transform(b, a, N)

print(h)

x = np.array([1, 0, 0, 1])

y = np.convolve(x, h)

print(y)