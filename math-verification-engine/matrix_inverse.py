import numpy as np

A=np.array([[1,2],[3,4]])

A_inv=np.linalg.inv(A)

print("矩阵:")
print(A)

print("逆矩阵:")
print(A_inv)

print("验证 A*A_inv:")
print(np.dot(A,A_inv))