# Calculus Limit Visualization - sin(x)/x

这是一个简单的 Python 项目，用于通过数值计算和图形可视化来验证数学中的经典极限：
$$\lim_{x \to 0} \frac{\sin(x)}{x} = 1$$

## 项目简介
本项目包含一个 Python 脚本，它执行以下操作：
1. **数值逼近**：通过不断减小 $x$ 的值，计算 $\frac{\sin(x)}{x}$ 的结果并打印输出。
2. **图形绘制**：使用 `matplotlib` 绘制函数图像，直观展示函数在 $x$ 趋近于 0 时的行为。

## 环境要求
在运行本项目之前，请确保你的电脑已安装 Python 3.x 以及以下第三方库：

- `numpy` (用于数学计算)
- `matplotlib` (用于绘图)

### 安装依赖
你可以使用以下命令安装所需的库：
```bash
pip install numpy matplotlib
