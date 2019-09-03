# 实战 人民币，数字转中文大写


han_list = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
unit_list = ["十", "百", "千"]


def divide(num):
    # 取整
    integer = int(num)
    # 取小数部分，并乘100后取整
    fraction = round((num - integer) * 100)
    return [str(integer), str(fraction)]
