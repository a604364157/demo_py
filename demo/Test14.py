import datetime
import time


def timeStamp(timeNum):
    timeStamp = float(timeNum / 1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)


base = '2020-01-01 00:00:00'
base_time = datetime.datetime.strptime(base, '%Y-%m-%d %H:%M:%S')
base_time = base_time + datetime.timedelta(seconds=1)
base_time_str = base_time.strftime("%Y-%m-%d %H:%M:%S")
print(base_time_str[-5:])
