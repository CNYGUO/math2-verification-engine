#验证导数定义
#f(x)=x^2
#导数应该是2x
def f (x):
    return x**2
def derivative_numeric(x,h):
    return (f(x+h)-f(x)) / h
#测试点
x = 2
print("验证 f(x)=x^2 在 x=2 的导数")
print("真实导数：",2*x)

print("\n数值验证结果：")

h_values = [1, 0.1, 0.01, 0.001, 0.0001, 0.00001]

for h in h_values :
    result = derivative_numeric(x,h)
    print(f"h={h:<10} 数值导数={result}")