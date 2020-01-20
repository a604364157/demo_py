import random

reds = [i for i in range(1, 34)]
blues = [i for i in range(1, 17)]


def run_two_color():
    """
    随机生成一组双色球号码
    :return: 列表
    """
    out = random.sample(reds, k=6)
    out.sort()
    return out + random.sample(blues, k=1)
