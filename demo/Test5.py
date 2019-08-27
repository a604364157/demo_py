# 元组
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(a)
b = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(b)

# 创建只有一个元素的元组
c = ("a",)
print(type(c))
# 这种方式会被认为是字符串，所以一个时也带上一个,
c = ("a")
print(type(c))
# 列表转元组
a = [1, 2, 3, 4, 5]
b = tuple(a)
print(b)

# 访问元组元素
print(b[0])
print(b[:1])

# 修改元组元素
# 元组不能单独修改元素，只能重新赋值

# 元组添加元素
b = b + (6, 7, 8, 9)
print(b)

# del()可以删除元组

# 元组和列表的区别类似于 java中的数组和list
# 列表可变，元组不可变。同时 python的列表和元组的特性和go是一样的


# dict字典（python中的映射数据结构，类似于java的map）
dict1 = {1: "a", 2: "b", 3: "c", 4: "d"}
print(dict1)
# {}代表空dict
empty_dict = {}
# 字典的key可以是不可变的任意类型(数字，字符串，元组) value允许各种结构
dict2 = {}
# 通过 fromkeys() 方法创建空字典
a = [1, 2, 3]
b = dict.fromkeys(a)
print(b)
# 通过dict()函数创建字典
a = dict(a=1, b=2)
print(a)

# 字典的基本操作
a = {1: "a", 2: "b", 3: "c"}
print(a)
# 添加新的键值对
a[4] = "b"
print(a)
# 修改
a[4] = "d"
print(a)
# 删除
del a[4]
print(a)
# 是否存在
print(2 in a)
print(2 not in a)

# dict函数
a = {1: "a", 2: "b", 3: "c"}
print(a.keys())
print(list(a.keys()))
print(a.values())
print(list(a.values()))
print(a.items())
print(list(a.items()))
# copy()函数
b = a.copy()
print(b)
# update()函数
a.update({1: "A"})
print(a)
# pop()函数 取出元素，并在原字典删除，不指定则是最后一个
print(a.pop(1))
print(a)
# popitem() 随机取出一个元素，并在原字典删除
# 实际上这个随机是假的，是取底层存储的最后一个
print(a.popitem())
print(a)
# setdefault()函数
# 设置默认值，如果已经存在，则不改变
a = {1: "a", 2: "b", 3: "c"}
a.setdefault(3, "C")
print(a)
a.setdefault(4, "d")
print(a)
# 可以使用字典来格式化字符串
a = "小明说：%(a)s，小红说%(b)s"
b = {"a": "你好呀", "b": "我很好，你也好"}
print(a % b)