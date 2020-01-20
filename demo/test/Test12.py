# 类的定义
from types import MethodType


class Person:
    """定义一个Person类"""
    name = ""
    age = 0
    sex = ""

    # 构造器(python中不能重载)
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def hello(self):
        print("hello " + self.name)

    @classmethod
    def say2(cls):
        print("你好" + cls.name)

    @staticmethod
    def say3(param):
        print("你好" + param)


# 类的使用
person = Person("蕊英", 18, "女")
person.age = 19
person.hello()
# 类类似对象，可以动态添加属性
person.aa = "aa"
print(person.__dict__)
# 动态添加函数
person.say = lambda self: print("你好" + self.name)
# python不会将调用对象绑定为第一个参数，所以要手动传参
person.say(person)
# 如果需要自动绑定调用对象，需要使用MethodType
person.say = MethodType(lambda self: print("你好" + self.name), person)
person.say()

# 类属性（通过类调用和通过实例对象调用）
print("类属性")
print(person.name)
print(Person.name)
Person.name = "123"
print(person.name)
print(Person.name)

# 实例函数
# 定义的hello()是一个实例函数
person.hello()
Person.hello(person)  # 需要传入实例对象

# 类函数
# 类函数在定义时需要加@classmethod
# 我们定义了一个类函数 say2()
Person.say2()

# 静态函数
# 静态函数在定义时需要加@staticmethod
# 我们定义了一个静态函数 say3()
# 静态函数并不会做绑定
Person.say3("蕊英")
