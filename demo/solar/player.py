# 春分，雨水，惊蛰，春分，清明，谷雨，立夏，小满，芒种，夏至，小暑，大暑
# 立秋，处暑，白露，秋分，寒露，霜降，立冬，小雪，大雪，冬至，小寒，大寒
import os
import time
import wave

import pygame


# pygame.mixer.music.load	加载音乐文件
# pygame.mixer.music.play	播放加载完成的音乐文件
# pygame.mixer.music.rewind	重新播放音频
# pygame.mixer.music.stop	停止播放
# pygame.mixer.music.pause	暂停播放
# pygame.mixer.music.unpause	回复播放
# pygame.mixer.music.fadeout	淡出
# pygame.mixer.music.set_volume	设置音量
# pygame.mixer.music.get_volume	获取音量
# pygame.mixer.music.get_busy	检查音乐是否正在播放
# pygame.mixer.music.set_pos	设置开始播放的位置
# pygame.mixer.music.get_pos	获取音乐已经播放的时间
# pygame.mixer.music.queue	将音乐文件放入待循环列表
# pygame.mixer.music.set_endevent	音乐播放完成时发送事件
# pygame.mixer.music.get_endevent	获取音乐播放完成发送的事件类型

def play_wav(name):
    file = wave.open(name, "rb")
    params = file.getparams()
    channels, width, framerate, frames = params[:4]
    file.close()
    pygame.mixer.init(framerate)
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()
    play_time = frames / float(framerate)
    time.sleep(play_time)
    pygame.mixer.music.stop()


def play_mp3(name):
    # 网上说这个样会语速失真
    # 我随便测了一个，发现没有
    # 可能跟比特率有关系
    pygame.mixer.init()
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()
    # 这里必须卡音乐等时常，需要获取音乐的时长
    time.sleep(10)
    pygame.mixer.music.stop()


def play_by_sys(name):
    # 这个在windows下会调用系统默认音乐播放工具播放
    os.system(name)


# play_wav("")
play_mp3("mp3\\芒种.mp3")
# play_by_sys("mp3\\芒种.mp3")
