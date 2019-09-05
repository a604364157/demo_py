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
