# if语句


# if/else
def test1():
    age = input("请输入你的年龄\n")
    age = int(age)
    if age >= 18:
        print("你已成年")
    else:
        print("你还未成年")


# False、None、0、""、()、[]、{} 这些值会被认为 False处理

# if嵌套
def test2():
    proof = int(input("输入驾驶员每 100ml 血液酒精的含量：\n"))
    if proof < 20:
        print("不是酒驾")
    else:
        if proof < 80:
            print("是酒驾")
        else:
            print("是醉驾")


def test3():
    # pass空语句
    s = int(input("请输入一个整数:\n"))
    if s > 0:
        print("是正数")
    elif s == 0:
        pass
    else:
        print("是负数")


def test4():
    # assert断言语句
    # 断言如果达不到条件，则会报AssertionError错误
    age = int(input("请输入您的年龄:\n"))
    assert 0 < age < 18
    print("你还未成年")


def test5():
    # while循环语句
    num = 1
    while num < 100:
        print(num)
        num += 1
    print("循环完成")


def test6():
    # for循环语句
    result = 0
    for i in range(101):
        result += i
    print(result)


# for遍历元组
def test7():
    a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    for aa in a:
        print(aa)


# for遍历列表
def test8():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for aa in a:
        print(aa)


# for遍历字典
def test9():
    a = {"a": 1, "b": 2, "c": 3}
    # 遍历键值对
    for k, v in a.items():
        print(k + "=" + str(v))
    # 遍历key
    for k in a.keys():
        print(k)
    # 遍历value
    for v in a.values():
        print(v)


# 循环结构中else用法
def test10():
    i = 0
    while i < 5:
        print(i)
        i += 1
    else:
        print(i)
    # for的else块会是循环最后一个值，while会是循环条件不成立的第一个值
    # 总体上循环块的else没有太多作用
    for i in range(5):
        print(i)
    else:
        print(i)


# 嵌套循环(99乘法表)
def test11():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("{:d}x{:d}={:d}  ".format(j, i, i * j), end="")
        print()


# for推导式
def test12():
    # 列表推导
    a = [x * x for x in range(10)]
    print(a)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    b = [x * x for x in range(10) if x % 2 == 0]
    print(b)  # [0, 4, 16, 36, 64]
    c = [(x, y) for x in range(5) for y in range(4)]
    print(c)
    # 元组推导
    a = (x for x in range(1, 10))
    # 是一个生成器对象，而不是元组
    print(a)
    # 转换为元组
    print(tuple(a))
    # 直接从生成器获取元组的元素
    a = (x for x in range(1, 10))
    for i in a:
        print(i, end="")
    print()
    # 使用next函数
    a = (x for x in range(1, 10))
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())
    # 字典推导式
    k = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}
    a = {key: value for key, value in k.items()}
    print(a)



# test1()
# test2()
# test3()
# test4()
# test5()
# test6()
# test7()
# test8()
# test9()
# test10()
# test11()
test12()
