import random
# import json

from web.models import TwoColorBall


def run_two_color():
    reds = [i for i in range(1, 34)]
    blues = [i for i in range(1, 17)]
    out = random.sample(reds, k=6)
    out.sort()
    return out + random.sample(blues, k=1)


def run_two_colors(times):
    if times is None:
        times = 1
    else:
        times = int(times)

    out = []
    for i in range(times):
        out.append(run_two_color())

    # return json.dumps(out, ensure_ascii=False)
    return out


def query_two_colors(start, end):
    if end is not None:
        balls = TwoColorBall.objects.filter(run_date__lte=end, run_date__rte=start)
    else:
        balls = TwoColorBall.objects.filter(run_date__exact=start)

    return balls


def run_big_lotto():
    reds = [i for i in range(1, 36)]
    blues = [i for i in range(1, 13)]
    out = random.sample(reds, k=5)
    out.sort()
    t = random.sample(blues, k=2)
    t.sort()
    return out + t


def run_big_lottos(times):
    if times is None:
        times = 1
    else:
        times = int(times)
    out = []
    for i in range(times):
        out.append(run_big_lotto())
    return out
