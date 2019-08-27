import sys
print(sys.getdefaultencoding())

# 字符串函数

# len()
s1 = "123456789呵呵"
print(len(s1))
print(len(s1.encode()))

# input() 控制台输入
# msg = input("请输入")
# print(msg)
# print(type(msg))

# print() 控制台打印
print("呵呵")
print("呵呵", "123")
# 多输出默认空格，通过sep替换
print("呵呵", "123", sep="")
# print() 会默认换行，如果不想换
print("123", end="")
print("456", end="")
print("789")

# print()默认输出到控制台，可以通过file指定到其他文件
f = open("test.txt", "w", encoding="utf-8")
print("春蚕到死丝方尽", file=f)
print("蜡炬成灰泪始干", file=f)
f.close()

# 字符串的格式化（转换符说明可以自行查询资料）
# %d，%i	转换为带符号的十进制形式的整数
# %o	转换为带符号的八进制形式的整数
# %x，%X	转换为带符号的十六进制形式的整数
# %e	转化为科学计数法表示的浮点数（e 小写）
# %E	转化为科学计数法表示的浮点数（E 大写）
# %f，%F	转化为十进制形式的浮点数
# %g	智能选择使用 %f 或 %e 格式
# %G	智能选择使用 %F 或 %E 格式
# %c	格式化字符及其 ASCII 码
# %r	使用 repr() 将变量或表达式转换为字符串
# %s	使用 str() 将变量或表达式转换为字符串
s2 = "你好"
print("小明说：%s" % s2)

# 指定最小长度(这里会自动在前面补空格)
print("小明说：%5s" % s2)

# 转义字符
# \	在行尾的续行符，即一行未完，转到下一行继续写
# \'	单引号
# \"	双引号
# \0	空
# \n	换行符
# \r	回车符
# \t	水平制表符，用于横向跳到下一制表位
# \a	响铃
# \b	退格（Backspace）
# \\	反斜线
# \0dd	八进制数，dd 代表字符，如 \012 代表换行
# \xhh	十六进制数，hh 代表字符，如 \x0a 代表换行


# 数据类型转换
# int(x)	将 x 转换成整数类型
# Iloat(x)	将 x 转换成浮点数类型
# complex(real，[,imag])	创建一个复数
# str(x)	将 x 转换为字符串
# repr(x)	将 x 转换为表达式字符串
# eval(str)	计算在字符串中的有效 Python 表达式，并返回一个对象
# chr(x)	将整数 x 转换为一个字符
# ord(x)	将一个字符 x 转换为它对应的整数值
# hex(x)	将一个整数 x 转换为一个十六进制字符串
# oct(x)	将一个整数 x 转换为一个八进制的字符串
