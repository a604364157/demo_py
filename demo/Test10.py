# 函数


# 函数定义
def s_max(x, y):
    """
    获取两个数较大的数
    :param x: 数字1
    :param y: 数字2
    :return: 较大的数字
    """
    z = x if x > y else y
    return z


# 形式参数和实际参数
def demo1(obj):
    # 这里的obj就是形式参数
    print(obj)


a = "123456"
# 这里调用demo1，传入的参数a就是实际参数
demo1(a)


# 参数传递有两种：值传递和引用传递
# 值传递，实际参数不会因为形式参数改变而改变
# 引用传递，实际参数会因为形参改变
# 不可变的对象为值传递（字符串、数字、元组）


# 位置参数
def demo2(x, y):
    print(x + y)


# 实参和形参数量必须一致
# 实参和形参位置必须一致
demo2(1, 2)

# 关键字参数
# 使用定义的形参来对参数赋值
# 使用关键字参数时，如果有位置参数，位置参数必须在关键字前面
demo2(y=1, x=2)
# demo2(1, x=2) 异常
demo2(1, y=2)


# 默认参数
# 这样定义，在调用该函数时，y可以不传，会默认为2
def demo3(x, y=2):
    print(x + y)


demo3(1)


# 可变参数，在形参前加*
# 这种形式表示接受任意多个实际参数，并将其放到一个元组中
def demo4(*x):
    print(x)


demo4(1, 2, 3, 4)


# 可变参数，在形参前加**
# 这种形式可以接收任意多个以关键字参数赋值的实际参数，并将其放到一个字典中
def demo5(**x):
    print(x)


demo5(a=1, b=2, c=3)

# demo4和demo5会自动将参数构造为元组和字典，但是它们也能直接接收元组和字典参数
# 需要在实际参数前加* 进行参数收集
a = (1, 2, 3, 4, 5)
demo4(*a)
a = {'a': 1, 'b': 2, 'c': 3}
demo5(**a)


# 函数的高级用法
# 使用函数变量

# 定义一个计算乘方的函数
def _pow(base, e):
    return base ** e


test_fun = _pow
print(test_fun(2, 2))


# 使用函数作为函数的形参
def _map(data, fn):
    out = []
    for i in data:
        out.append(fn(i, i))
    return out


data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(_map(data, _pow))


# 使用函数作为返回值
def get_math_func(type):
    def _sum(a, b):
        return a + b

    def _prod(a, b):
        return a * b

    if type == "s":
        return _sum
    else:
        return _prod


test = get_math_func("s")
print(test(1, 2))
test = get_math_func("p")
print(test(1, 2))


# 闭包
def nth_pow(e):
    def ex(base):
        return base ** e

    return ex


a = nth_pow(2)  # 计算2次方
b = nth_pow(3)  # 计算3次方
print(a(2))
print(b(2))

# 闭包是一种函数的高级用法，但实际用的少，看个人编码习惯
# 主要是能看懂
