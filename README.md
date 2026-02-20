# math2-verification-engine
# 数二数学验证工程（Math2 Verification Engine）
## 项目简介
本项目用于通过 Python 数值计算验证考研数学二（高等数学与线性代数）的核心数学概念。
将抽象数学公式转化为可计算程序，加深对极限、导数、积分和矩阵等内容的理解。
项目目标：
强化数学二核心概念理解
建立数学与工程计算之间的联系
提升编程能力（Python）
为研究生阶段机械建模与仿真打下基础
---
## 项目结构
math2-verification-engine/
limits/                 极限验证  
derivatives/            导数验证  
integrals/              积分验证  
linear_algebra/         线性代数验证  
README.md               项目说明  
---
## 验证内容
### 1. 极限验证（Limits）
示例：
验证：
lim sin(x)/x = 1
通过数值计算观察 x → 0 时函数值变化。
文件：
limits/limit_numeric.py
---
### 2. 导数定义验证（Derivatives）
数学定义：
f'(x) = lim(h→0) (f(x+h)−f(x))/h
示例：
验证：
f(x)=x²  
f'(x)=2x
文件：
derivatives/derivative_definition.py
---

### 3. 定积分验证（Integrals）
使用黎曼和（Riemann Sum）验证积分定义。
示例：
∫₀¹ x² dx = 1/3
文件：
integrals/riemann_sum.py
---
### 4. 矩阵运算验证（Linear Algebra）
验证：
矩阵逆  
矩阵乘法  
文件：
linear_algebra/matrix_inverse.py
---
## 技术栈
Python 3  
numpy  
matplotlib  
---
## 项目意义（考研与工程方向）
本项目将数学公式转化为计算机验证过程，有助于：
深入理解考研数学二
建立工程计算思维
为机械工程仿真（Abaqus、Fluent）打下数学基础
---
## 作者信息
本科专业：
机械工程
目标：
考研方向：机械工程专硕
发展方向：
机械系统设计  
仿真分析  
系统工程  
---
## 项目持续更新计划
未来将增加：
泰勒展开验证  
微分方程数值解  
特征值计算  
机械振动数学模型验证  
---
GitHub 用于长期记录数学与工程学习过程。
