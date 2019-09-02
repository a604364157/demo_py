import random
# import json

from web.models import TwoColorBall


def run_two_color():
    reds = []
    for i in range(33):
        reds.append(i + 1)

    blues = []
    for i in range(12):
        blues.append(i + 1)

    out = []
    j = 32
    for i in range(6):
        rand = random.randint(0, j)
        out.append(reds.pop(rand))
        j -= 1

    out.sort()
    rand = random.randint(0, 11)
    out.append(blues.pop(rand))
    return out


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
