# 封装


class User:

    @staticmethod
    def __hide(self):
        print("这是隐藏的函数")

    def __init__(self) -> None:
        self.__name = ""
        self.__age = 0

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    name = property(get_name, set_name)

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    age = property(get_age, set_age)


u = User()
u.name = "蕊英"
u.age = 18
print(u.__dict__)


# 继承
# 继承的写法就是Class(父类1，父类2)
# python是可以多继承的，多继承比较复杂，而且处理不好还容易产生莫名的错误
# 编码中尽量不要使用多继承
# python中写父类中同名函数及为重写
class Student(User):

    def __init__(self) -> None:
        super().__init__()
        self.__score = 0

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

    score = property(get_score, set_score)


# 重写
# python中写父类中同名函数及为重写
class Parent:
    def foo(self):
        print("父类的foo函数")


class Child(Parent):
    def foo(self):
        print("子类的foo函数")

    def boo(self):
        print("子类的boo函数")
        self.foo()
        Parent.foo(self)


c = Child()
c.boo()