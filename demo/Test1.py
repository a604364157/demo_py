import cmath

# hello
print("hello 蕊英")

# 变量
a = 5
print(a)
a = "hello"
print(a)
print(type(a))
a = 9999999999999999999
print(type(a))
a = None
print(a)

# 整形的4种形式（2，8，10，16进制）
hex_a = 0x13  # 16
print(hex_a)
bin_a = 0b111  # 2
print(bin_a)
oct_a = 0o54  # 8
oct_b = 0O17  # 8
print(oct_a)
print(oct_b)

# 允许_作为数值的连接符，增加可读性(要3.7才能支持)
# a = 123_456_789
# print(a)
# b = 123.4_56
# print(b)

# 浮点型
af = 123.123
print(af)
print(type(af))
# 科学计数(2.2*10的2次方)
af = 2.2e2
print(af)

# 复数
ac = 3 + 0.2j
print(ac)
print(type(ac))
ab = 4 + 0.1j
print(ac + ab)

ac = cmath.sqrt(-1)
print(ac)

# 字符串
s1 = 'abcdefg'
s2 = "呵呵"
print(s1)
print(s2)
# 特殊字符转义(双引号包裹，可以转义单引号，相反亦可)
s3 = "I'm a coder"
print(s3)
s4 = 'ruiying:"hello"'
print(s4)
# \ 进行转义
s5 = 'I\'m a coder'
print(s5)

# 换行的转义
s6 = 'qwerty' \
     '12345'
print(s6)
# 表达式换行也需要转义
n = 1 + 2 + 3 + \
    4
print(n)

# 长字符
s7 = '''1233456789
12354556768
123434556'''
print(s7)

# 消除\的作用
s8 = r"D:\demo\python"
print(s8)

# 当存在需要转义的\和不转义同时存在
s9 = r'D:\demo\python is' '\"dir\"'
print(s9)

# bytes
b1 = bytes()
b2 = b''
b3 = b'hello'
print(type(b1))
print(type(b2))
print(b3[0])
print(b3[2:4])
print(b3)
# bytes函数将字符转byte
b4 = bytes("呵呵呵呵呵呵", encoding="utf-8")
b5 = bytes("呵呵呵呵呵呵".encode("utf-8"))
print(b4)
print(b5)
b6 = b5.decode("utf-8")
print(b6)

# bool
bo1 = False
bo2 = True
