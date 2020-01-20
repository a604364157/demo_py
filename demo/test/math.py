# 加号 +
# 减号 -
# 除号 /
# 乘号 *
# 指数 **
# 对数 log()
# e的指数次幂 exp()
# 虚数单位 sympy.I
# 自然对数的底e sympy.E
# 无穷大 sympy.oo
# 圆周率 sympy.pi
import sympy


# 一元二次方程
def t1():
    x = sympy.symbols('x')
    a = sympy.solve([x ** 2 + 7 * x + 12], [x])
    print(a)


# 二元一次方程
def t2():
    x, y = sympy.symbols('x y')
    a = sympy.solve([3 * x - 2 * y - 3, x + 2 * y - 5], [x, y])
    print(a)


# 分式方程
def t3():
    x = sympy.symbols('x')
    a = sympy.solve([((x + 1) / x + 1 / (x - 2)) - 1], [x])
    print(a)


# 代数运用（^2代表平方）
# 已知x+y=0.2，x+3y=1求x^2+4xy+4y^2？
def t4():
    x, y = sympy.symbols("x y")
    a = sympy.solve([x + y - 0.2, x + 3 * y - 1], [x, y])
    print(a)
    x = a[x]
    y = a[y]
    re = x ** 2 + 4 * x * y + 4 * y ** 2
    print(re)


if __name__ == '__main__':
    t1()
    t2()
    t3()
    t4()
