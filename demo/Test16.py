# type()函数，动态创建类
import enum

User = type("User", (object,), dict(name="蕊英", age=18))
u = User()
print(u.name)

# 枚举
OpType = enum.Enum("OpType", ("ADD", "DEL", "MOD", "QRY"))

print(OpType.ADD)
print(OpType.ADD.name)
print(OpType.ADD.value)


class OpType(enum.Enum):
    ADD = 1
    DEL = 2
    MOD = 3
    QRY = 4


print(OpType.ADD)
print(OpType.ADD.name)
print(OpType.ADD.value)
