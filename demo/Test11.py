# lambda表达式
# lambda [parameter_list] : 表达式


def get_math(t):
    if t == "s":
        return lambda a, b: a + b
    else:
        return lambda a, b: a * b


_sum = get_math("s")
print(_sum(1, 2))
_sum = get_math("p")
print(_sum(1, 2))
