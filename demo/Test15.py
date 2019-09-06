# __slots__：限制类实例动态添加属性和方法
from types import MethodType


class User:
    __slots__ = ("__name", "__age", "get_all")

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


# 我们创建User是现在了属性和方法
u = User()
u.name = "蕊英"
print(u.name)
# u.a = "123" 报错
u.get_all = MethodType(lambda self: (self.name, self.age), u)
print(u.get_all())
