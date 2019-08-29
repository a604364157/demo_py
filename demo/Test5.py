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

# set 集合 不重复，无序
print("set集合")
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4}
print(a)
set1 = set("1234567891234")
print(set1)
t = [1, 2, 3, 4, 5]
set2 = set(t)
print(set2)
t = (1, 2, 3, 4, 5)
set3 = set(t)
print(set3)
# 因为set无序，所以不能通过索引访问，可以循环
for v in a:
    print(v, end="")
print()
# set基本操作
a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# 添加元素
a.add(10)
a.add((11, 12))
print(a)
# 删除元素
a.remove(10)
a.remove((11, 12))
print(a)
# a.remove(10) 报错
a.discard(10)  # 删除失败不报错
print(a)
# set集合的 交集，并集，差集，对称差集
a = {1, 2, 3, 4, 5, 6, 7}
b = {4, 5, 6, 7, 8, 9, 0}
# 交集
print(a & b)
# 并集
print(a | b)
# 差集
print(a - b)
# 对称差集(相当于相互差集取并集)
print(a ^ b)

# set() 相关函数
a = {1, 2, 3, 4, 5}
a.add(6)  # 添加元素
a.clear()  # 清空元素
b = a.copy()  # 克隆a给b
c = a.difference(b)  # 将a中有，而b中没有的元素给c
a.difference_update(b)  # 从a中删除与b中相同的元素
a.discard(1)  # 删除元素
c = a.intersection(b)  # 取a和b的交集给c
a.intersection_update(b)  # 取a和b的交集并重新赋值给a
a.isdisjoint(b)  # 判断a和b是否有交集
a.issubset(b)  # 判断a是否时b的子集
a.issuperset(b)  # 判断b是否是a的子集
t = a.pop()  # 取出一个元素，赋值给t，并从原集合删除
a.remove(1)  # 删除a中的元素，元素不存在会报错
c = a.symmetric_difference(b)  # 取出a和b中互不相同的元素给c
a.symmetric_difference_update(b)  # 取出a和b中互不相同的元素,并更新a
c = a.union(b)  # 取a和b的并集给c
a.update(b)  # 将b（可以是列表或集合）到a中

# frozenset 不可变的集合(操作和set一样，但是所有会改变原set的函数都不支持)
f = frozenset("123456789")
