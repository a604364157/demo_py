# 跳过了异常处理和内置函数的讲解

# 本文件讲解常见模块的用法
import json
import os
import random
import sys
import time


def t1():
    # 显示本地字节序的指示符
    print(sys.byteorder)
    # 显示Python解释器有关的版权信息
    print(sys.copyright)
    # 显示Python解释器在磁盘上的存储路径
    print(sys.executable)
    # 显示当前系统上保存文件所用的字符集。
    print(sys.getfilesystemencoding())
    # 显示Python整数支持的最大值
    print(sys.maxsize)
    # 显示Python解释器所在平台
    print(sys.platform)
    # 显示当前Python解释器的版本信息。
    print(sys.version)
    # 返回当前Python解释器的主版本号。
    print(sys.winver)


def t2():
    # 显示导入依赖模块的操作系统的名称
    print(os.name)
    # 获取PYTHONPATH环境变量的值
    print(os.getenv('PYTHONPATH'))
    # 返回当前系统的登录用户名
    print(os.getlogin())
    # 获取当前进程ID
    print(os.getpid())
    # 获取当前进程的父进程ID
    print(os.getppid())
    # 返回当前系统的CPU数量
    print(os.cpu_count())
    # 返回路径分隔符
    print(os.sep)
    # 返回当前系统的路径分隔符
    print(os.pathsep)
    # 返回当前系统的换行符
    print(os.linesep)
    # 返回适合作为加密使用的、最多3个字节组成的bytes
    print(os.urandom(3))


def t3():
    # 生成范围为0.0≤x<1.0 的伪随机浮点数
    print(random.random())
    # 生成范围为2.5≤x<10.0 的伪随机浮点数
    print(random.uniform(2.5, 10.0))
    # 生成呈指数分布的伪随机浮点数
    print(random.expovariate(1 / 5))
    # 生成从0 到9 的伪随机整数
    print(random.randrange(10))
    # 生成从0 到100 的随机偶数
    print(random.randrange(0, 101, 2))
    # 随机抽取一个元素
    print(random.choice(['Python', 'Swift', 'Kotlin']))
    book_list = ['Python', 'Swift', 'Kotlin']
    # 对列表元素进行随机排列
    random.shuffle(book_list)
    print(book_list)
    # 随机抽取4 个独立的元素
    print(random.sample([10, 20, 30, 40, 50], k=4))


def t4():
    # 将当前时间转换为时间字符串
    print(time.asctime())
    # 将指定时间转换时间字符串，时间元组的后面3个元素没有设置
    print(time.asctime((2018, 2, 4, 11, 8, 23, 0, 0, 0)))  # Mon Feb  4 11:08:23 2018
    # 将以秒数为代表的时间转换为时间字符串
    print(time.ctime(30))  # Thu Jan  1 08:00:30 1970
    # 将以秒数为代表的时间转换为struct_time对象。
    print(time.gmtime(30))
    # 将当前时间转换为struct_time对象。
    print(time.gmtime())
    # 将以秒数为代表的时间转换为代表当前时间的struct_time对象
    print(time.localtime(30))
    # 将元组格式的时间转换为秒数代表的时间
    print(time.mktime((2018, 2, 4, 11, 8, 23, 0, 0, 0)))  # 1517713703.0
    # 返回性能计数器的值
    print(time.perf_counter())
    # 返回当前进程使用CPU的时间
    print(time.process_time())
    # time.sleep(10)
    # 将当前时间转换为指定格式的字符串
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    st = '2018年3月20日'
    # 将指定时间字符串恢复成struct_time对象。
    print(time.strptime(st, '%Y年%m月%d日'))
    # 返回从1970年1970年1月1日0点整到现在过了多少秒。
    print(time.time())
    # 返回本地时区的时间偏移，以秒为单位
    print(time.timezone)  # 在国内东八区输出-28800


def t5():
    # 将py对象转json串
    s = json.dumps({"a": 1, "b": 2, "c": 3})
    print(s)
    s = json.JSONEncoder().encode({"a": 1, "b": 2, "c": 3})
    print(s)


if __name__ == '__main__':
    # t1()
    # t2()
    # t3()
    # t4()
    t5()
