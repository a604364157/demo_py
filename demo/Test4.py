# 序列
s1 = "123456789"
print(s1[0], "==", s1[-9])
# 切片
s2 = s1[:2]  # 取序列的0到2区间
s3 = s1[::2]  # 原序列隔一个字符取一个，区间是整个
s4 = s1[:]  # 取整个原序列
print(s2)
print(s3)
print(s4)
# 序列相乘
print(s1 * 2)

# 检查元素是否存在于序列中
print("1" in s1)
print("1" not in s1)

# 列表
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ss = ["a", "b", "c", "d"]
# 将圆组转列表
a = ("a", 1, 0.1)
b = list(a)
print(a)
print(b)
# 使用 range函数
c = range(1, 5)
print(list(c))

# 删除列表
a = [1, 2, 3]
print(a)
del a
# print(a) 报错，未定义

# 给列表添加元素
print("给列表添加元素")
# append() 此函数只会将添加的内容作为一个元素添加
print("append()")
b = [1, 2, 3]
print(b)
b.append(4)
print(b)
b.append([5, 6])
print(b)
# extend() 此函数会将添加的内容解构
print("extend()")
c = [1, 2, 3]
c.extend((4, 5))
print(c)
c.extend([6, 7])
print(c)
# 插入元素 insert(),此函数追加元素类似append
print("插入元素 insert()")
d = [1, 3, 5]
d.insert(1, 2)
print(d)

# 删除列表元素
print("删除列表元素")
e = [1, 2, 3, 4, 5, 6]
# del() 按索引
print("del()")
del e[5]
print(e)
del e[0:3]
print(e)
# remove() 按元素值
print("remove()")
e = [1, 2, 3, 4, 5, 6]
e.remove(6)
print(e)
# count() 统计元素在列表的个数
if e.count(6):
    e.remove(6)
print(e)
# 清空列表
e.clear()

# 修改列表元素
print("修改列表元素")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[0] = 0
print(a)
a[-1] = 0
print(a)
a[1:3] = [0, 0]
print(a)
# 插入
a[3:3] = [0, 0, 0]
print(a)
# 删除
a[3:6] = []
print(a)
# 自动解构(对序列而言)
a[0:3] = "123"
print(a)

# 常用函数
print("常用函数")
# count() 统计元素出现次数
print("count()")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a.count(1))
# index() 获取索引
print("index()")
print(a.index(1))
# 索引指定区间(只是减少搜索范围，不会改变索引值)
print(a.index(5, 4, 9))
# pop() 取出指定索引的元素，不指定则为最后一个，并返回，原列表中移除
# 利用append()和pop()实现栈（先入后出）
print("pop()")
print(a.pop())
print(a)
# reverse() 元素逆序
print("reverse()")
print(a)
a.reverse()
print(a)
# sort() 排序
print("sort()")
a.sort()
print(a)
# sort() 还可以指定排序规则
# sort(key=len, reverse=True) 按长度，反序

