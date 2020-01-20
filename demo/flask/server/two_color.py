import random


def run_two_color():
    reds = [i for i in range(1, 34)]
    blues = [i for i in range(1, 17)]
    out = random.sample(reds, k=6)
    out.sort()
    return out + random.sample(blues, k=1)
