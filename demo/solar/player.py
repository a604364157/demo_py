# 春分，雨水，惊蛰，春分，清明，谷雨，立夏，小满，芒种，夏至，小暑，大暑
# 立秋，处暑，白露，秋分，寒露，霜降，立冬，小雪，大雪，冬至，小寒，大寒
import os

from playsound import playsound


def play_mp3(name):
    playsound(name)


def play_sys(name):
    # 这个在windows下会调用系统默认音乐播放工具播放
    os.system(name)


play_mp3("mp3/9.mp3")
# play_sys("mp3\\9.mp3")
