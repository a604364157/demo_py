# 字符串常用方法

# 1字符串拼接
s1 = "hello " 'world'
print(s1)
s1 = "hello " + 'world'
print(s1)

# 和java不同的是，字符串不能直接和其他类型拼接
s1 = "123"
num = 456
# print(s1+num) 报错
print(s1 + str(num))
print(s1 + repr(num))

# 2字符串截取
s1 = "123456789"
print(s1[2])
print(s1[-2])
# 切片string[start : end : step]
print(s1[2:])
print(s1[:2])
print(s1[::2])
# 包含
print("123" in s1)
print("123" not in s1)
# min max
print(max(s1))
print(min(s1))

# 3字符串分割
s1 = "1|2|3|4|5|6|7|8|9"
print(s1.split("|"))
print(s1.split("|", 3))

# join合并字符串
# newstr = str.join(iterable) str是连接的分割符，iterable是连接的数据，允许序列，列表，元组等
s1 = "|"
print(s1.join("123456789"))
print(s1.join(("1", "2", "3")))
print(s1.join(["1", "2", "3"]))
print(s1.join({"1", "2", "3"}))

# count函数，统计出现次数
print("count")
s1 = "123456789"
print(s1.count("1"))
print(s1.count("1", 3, 5))  # 后面两参数是检查范围

# find函数，寻找索引，没有则-1
print("find")
print(s1.find("9"))
print(s1.find("0"))
print(s1.find("9", 5, 9))
print(s1.rfind("1"))  # 从右边开始检索，但索引值不变

# index()函数
# 其实和find基本一样，不一样的地方是，如果不存在不会返回-1而是报错

# startswith & endswith
print("startswith & endswith")
s1 = "123456789"
print(s1.startswith("1"))
# 指定索引位置开始检索
print(s1.startswith("2", 1))
print(s1.endswith("9"))

# 字符串的大小写转换
print("大小写")
s1 = "abcdefg"
print(s1.title())  # 将每个单词首字母大小，其他小写
print(s1.upper())
s1 = "ABC"
print(s1.lower())

# 去掉空格
print("去空格")
s1 = " ab cd efg "
print(s1.strip())  # 左右空格
print(s1.lstrip())  # 左空格
print(s1.rstrip())  # 右空格
# 可以给参数，有参数则消除参数模板的字符，用于去除特殊字符
s1 = "\tabc\t"
print(s1)
print(s1.strip("\t"))

# format()
# <	数据左对齐。
# >	数据右对齐。
# =	数据右对齐，同时将符号放置在填充内容的最左侧，该选项只对数字类型有效。
# ^	数据居中，此选项需和 width 参数一起使用。

# +	正数前加正号，负数前加负号。
# -	正数前不加正号，负数前加负号。
# 空格	正数前加空格，负数前加负号。
# #	对于二进制数、八进制数和十六进制数，使用此参数，各进制数前会分别显示 0b、0o、0x前缀；反之则不显示前缀

# s	对字符串类型格式化。
# d	十进制整数。
# c	将十进制整数自动转换成对应的 Unicode 字符。
# e 或者 E 	转换成科学计数法后，再格式化输出。
# g 或 G	自动在 e 和 f（或 E 和 F）中切换。
# b	将十进制数自动转换成二进制表示，再格式化输出。
# o	将十进制数自动转换成八进制表示，再格式化输出。
# x 或者 X	将十进制数自动转换成十六进制表示，再格式化输出。
# f 或者 F	转换为浮点数（默认小数点后保留 6 位），再格式化输出。
# %	显示百分比（默认显示小数点后 6 位）。

# 转码
s = "呵呵呵呵呵呵呵呵"
ss = s.encode()
print(ss)
sss = ss.decode()
print(sss)
ss = s.encode("gbk")
print(ss)
sss = ss.decode("gbk")
print(sss)
