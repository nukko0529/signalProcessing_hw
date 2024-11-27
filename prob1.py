import numpy as np

def f(x):
    phi_1 = 1j * 3 * np.pi * x
    phi_2 = -(1j * 3 * np.pi * x)
    return (2 + 3j) * np.exp(phi_1) + (2 - 3j) * np.exp(phi_2)

print("f(1) = ")
print(f(1.0))
print("\n")
print("f(1.5) = ")
print(f(1.5))
print("\n")
print("f(2) = ")
print(f(2.0))
print("\n")