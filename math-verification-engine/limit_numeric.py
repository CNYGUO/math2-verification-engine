import numpy as np

def f(x):
    return np.sin(x)/x

x0 = 0.0001

print("验证极限 sin(x)/x → 1")

for x in [1,0.1,0.01,0.001,0.0001]:
    print(f"x={x:<10} value={np.sin(x)/x}")