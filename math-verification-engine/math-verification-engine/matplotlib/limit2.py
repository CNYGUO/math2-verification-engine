import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)/x

# 准备两个空列表来存数据
x_values = [1, 0.1, 0.01, 0.001, 0.0001]
y_values = [f(x) for x in x_values]

# 绘图：'o-' 表示圆点连线，'o' 表示只画圆点
plt.plot(x_values, y_values, 'o-') 

plt.title("Limit sin(x)/x")
plt.show()