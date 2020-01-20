# 给定 4，应该输出如下形式的数据
# 01 12 11 10
# 02 13 16 09
# 03 14 15 08
# 04 05 06 07
# 给定 5，应该输出如下形式的数据
# 01 16 15 14 13
# 02 17 24 23 12
# 03 18 25 22 11
# 04 19 20 21 10
# 05 06 07 08 09
# 绕圈圈填数输入


def pring(size: int):
    # 先生成一个二维数组，元数据为0
    array = [[0] * size]
    for i in range(size - 1):
        array += [[0] * size]
    # 控制绕圈方向
    orient = 0
    j = 0
    k = 0
    # 本质上还是1到size*size的所有数字，只是数字的位置需要控制
    # 我们已经生成了一个二维数组，成像为正方形
    # 从[0][0]的位置开始填充1,[1][0]填充2类推
    # 填充到关键位置需要转向，关键位置刚好是size长度
    for i in range(1, size * size + 1):
        array[j][k] = i
        # 方向控制
        if j + k == size - 1:
            # 这个条件是位于转轴
            if j > k:
                # 左下角
                orient = 1
            else:
                # 右上角
                orient = 2
        elif j == k and k >= size / 2:
            orient = 3
        elif j == k - 1 and k <= size / 2:
            orient = 0
        # 下一个填充的坐标
        if orient == 0:
            j += 1
        elif orient == 1:
            k += 1
        elif orient == 2:
            k -= 1
        elif orient == 3:
            j -= 1

    for i in range(size):
        for j in range(size):
            print("%02d " % array[i][j], end="")
        print()


if __name__ == '__main__':
    pring(9)
