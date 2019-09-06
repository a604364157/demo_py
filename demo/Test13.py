# 类属性封装，描述符


class Demo:

    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def __get__(self, instance, owner):
        print("调用了get")
        return self.a

    def __set__(self, instance, value):
        print("调用了set")
        self.a = value

    def __delete__(self, instance):
        print("调用了delete")
        del self.a


class Mclass:
    x = Demo(1, 2)
    y = 3


# Demo类定义了描述符get，set
# 那么读取类时，都会调用 get
# 设置类时，调用set
m = Mclass()
print(m.x)
m.x = 2
print(m.x)
del m.x


# property() 函数
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getsize(self):
        return self.width, self.height

    def setsize(self, size):
        self.width, self.height = size

    def delsize(self):
        self.width, height = 0, 0

    # 使用property(param1 = 读取绑定， param2 = 写入绑定，param3=删除绑定，param4=说明文档)
    size = property(getsize, setsize, delsize, "测试属性")


# 获取属性说明
print(Rectangle.size.__doc__)
help(Rectangle.size)

r = Rectangle(2, 3)
print(r.size)
r.size = 3, 4
print(r.size)


# 通过装饰器方式
class Rect:
    def __init__(self, value):
        self.__size = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @size.deleter
    def size(self):
        self.__size = 0


r = Rect(2)
print(r.size)
r._size = 3
print(r.size)
del r.size
print(r.size)
