# lambda表达式
# lambda [parameter_list] : 表达式
import functools


def get_math(t):
    if t == "s":
        return lambda a, b: a + b
    else:
        return lambda a, b: a * b


_sum = get_math("s")
print(_sum(1, 2))
_sum = get_math("p")
print(_sum(1, 2))


# map()函数
# map(function, iterable)
def test1():
    a = [1, 2, 3, 4, 5]
    b = map(lambda x: x + 1, a)
    # map()返回一个map对象，需要转换
    b = list(b)
    print(b)
    # map()也可以传入多个迭代对象
    c = map(lambda x, y: x + y, a, b)
    print(list(c))


# filter()函数
# filter(function, iterable)
def test2():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = filter(lambda x: x % 2 == 0, a)
    # 同样返回filter对象，需要转一下
    b = list(b)
    print(b)
    # 不能迭代多个对象


# reduce()函数
# reduce(function, iterable)
def test3():
    a = [1, 2, 3, 4, 5]
    # 计算 1*2*3*4*5
    b = functools.reduce(lambda x, y: x * y, a)
    print(b)


test1()
test2()
test3()
