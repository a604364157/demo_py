# 立春，雨水，惊蛰，春分，清明，谷雨，立夏，小满，芒种，夏至，小暑，大暑
# 立秋，处暑，白露，秋分，寒露，霜降，立冬，小雪，大雪，冬至，小寒，大寒
import datetime
import os
import random
import threading
import time
from mutagen.mp3 import MP3
import wave

import pygame  # pip install pygame


class PlayException(Exception):
    pass


def show_time_t(all_time: float):
    t = threading.Thread(target=show_time, args=(all_time,))
    t.start()


def show_time(all_time: float):
    all_time = int(all_time)
    base = '2020-01-01 00:00:00'
    base_time = datetime.datetime.strptime(base, '%Y-%m-%d %H:%M:%S')
    while all_time > 0:
        base_time = base_time + datetime.timedelta(seconds=1)
        base_time_str = base_time.strftime("%Y-%m-%d %H:%M:%S")
        print(base_time_str[-5:])
        time.sleep(1)
        all_time -= 1


def show_lrc_t(name: str):
    t = threading.Thread(target=show_lrc, args=(name,))
    t.start()


def show_lrc(name: str):
    name = name[:-3] + "lrc"
    lrc_dict = {}
    try:
        file = open(name, "r", encoding="utf-8")
    except FileNotFoundError:
        print("未找到歌词文件：" + name)
        return
    music_lrc_list = file.readlines()
    # 遍历每一行歌词
    for music_lrc_line in music_lrc_list:
        # 对每一行歌词进行切割
        music_lrc_time = music_lrc_line.split(']')
        music_lrc = music_lrc_time.pop()
        # 处理每一行歌词的时间
        for lrc_time in music_lrc_time:
            # 取出每一行的时间
            lrc_time_list = lrc_time[1:]
            # 处理时间，转为float类型
            time_list = lrc_time_list.split(':')
            # 这里是因为歌词里存在一些[]内不是时间的内容，这里捕获掉
            # 使用0.0作为key，0.0会被后面覆盖掉
            try:
                times = float(time_list[0]) * 60 + float(time_list[1])
            except ValueError:
                times = 0.0
            lrc_dict[times] = music_lrc
    time_sort = list(lrc_dict)
    time_sort.sort()
    time.sleep(time_sort[0])
    time_sleep = time_sort[0]
    for i in time_sort:
        print(lrc_dict[i])
        time.sleep(i - time_sleep)
        time_sleep = i


def _play_mp3(name: str):
    # 这个init()需要给一个参数，不然容易语数失真
    # 可能是我测试的资源的原因，暂未发现失真
    pygame.mixer.init()
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()
    # 这里获取时长
    play_time = MP3(name).info.length
    # 异步打印剩余时长
    show_time_t(play_time)
    # 异步打印歌词
    show_lrc_t(name)
    time.sleep(play_time)
    pygame.mixer.music.stop()


# pygame.mixer.music.load加载音乐文件
# pygame.mixer.music.play播放加载完成的音乐文件
# pygame.mixer.music.rewind重新播放音频
# pygame.mixer.music.stop停止播放
# pygame.mixer.music.pause暂停播放
# pygame.mixer.music.unpause回复播放
# pygame.mixer.music.fadeout淡出
# pygame.mixer.music.set_volume设置音量
# pygame.mixer.music.get_volume获取音量
# pygame.mixer.music.get_busy检查音乐是否正在播放
# pygame.mixer.music.set_pos设置开始播放的位置
# pygame.mixer.music.get_pos获取音乐已经播放的时间
# pygame.mixer.music.queue将音乐文件放入待循环列表
# pygame.mixer.music.set_endevent音乐播放完成时发送事件
# pygame.mixer.music.get_endevent获取音乐播放完成发送的事件类型


def _play_wav(name: str):
    wav_file = wave.open(name, "rb")
    params = wav_file.getparams()
    channels, samp_width, framerate, frames = params[:4]
    wav_file.close()
    pygame.mixer.init(framerate)
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()
    play_time = frames / float(framerate)
    time.sleep(play_time)
    pygame.mixer.music.stop()


def _play_by_sys(name: str):
    # 这个在windows下会调用系统默认音乐播放工具播放
    os.system(name)


def play_music(name: str):
    if name.lower().endswith("mp3"):
        _play_mp3(name)
    elif name.lower().endswith("wav"):
        _play_wav(name)
    else:
        _play_by_sys(name)


def main():
    dirs = os.listdir("mp3")
    random.shuffle(dirs)
    for i in dirs:
        # if i.lower().endswith(".mp3"):
        if i.lower() == "一个人挺好.mp3":
            print("正在播放《" + i + "》")
            play_music("mp3/" + i)


if __name__ == '__main__':
    main()
