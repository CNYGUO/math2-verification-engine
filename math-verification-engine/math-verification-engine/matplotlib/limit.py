import numpy as np
import matplotlib.pyplot as plt # 习惯上放在最开头

def f(x):
    # 使用 np.where 处理 x=0 的情况，防止报错
    return np.sin(x)/x

# 1. 生成 100 个从 -10 到 10 之间的点
x_curve = np.linspace(-10, 10, 100) 
y_curve = f(x_curve)

# 2. 绘图
plt.plot(x_curve, y_curve, label="sin(x)/x")

# 3. 把你刚才循环里的那些特殊点也点上去（用散点图 'o'）
special_x = np.array([1, 0.1, 0.01, 0.001, 0.0001])
plt.plot(special_x, f(special_x), 'ro', label="Points from loop") # 'ro' 表示红色的圆点

plt.legend() # 显示图例
plt.grid(True) # 显示网格
plt.show()