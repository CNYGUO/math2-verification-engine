def f(x):
    return x**2

def riemann_sum(n):
    a,b=0,1
    dx=(b-a)/n
    s=0

    for i in range(n):
        x=a+i*dx
        s+=f(x)*dx

    return s

for n in [10,100,1000,10000]:
    print(n, riemann_sum(n))

print("真实值:",1/3)