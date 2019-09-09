# 跳过了异常处理和内置函数的讲解

# 本文件讲解常见模块的用法
import os
import random
import sys


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


if __name__ == '__main__':
    # t1()
    # t2()
    t3()
