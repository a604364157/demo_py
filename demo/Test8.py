# 实战 人民币，数字转中文大写


han_list = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
unit_list = ["十", "百", "千"]
decimal_unit_list = ["角", "分"]


def divide(num: float):
    return [str(int(num)), str(round((num - integer) * 100))]


def four_to_hanstr(num_str: str):
    flag = False
    result = ""
    num_len = len(num_str)
    # 遍历字符
    for i in range(num_len):
        ii = int(num_str[i])
        if flag and ii == 0:
            flag = False
            continue
        if ii == 0:
            flag = True
        if i != num_len - 1 and ii:
            result += han_list[ii] + unit_list[num_len - 2 - i]
        else:
            result += han_list[ii]
    if _is_all_zero(num_str):
        # 截掉最后的零
        result = result[:1]
    return result


def _is_all_zero(num_str: str):
    # 判断4位字符除首位外，全是零
    for i in num_str[1:]:
        if int(i) != 0:
            return False
    return True


def integer_to_str(num_str: str):
    str_len = len(num_str)
    if str_len > 12 or num_str.startswith("-"):
        print("数字太大了，超出计算范围")
        return
    # 包含亿
    elif str_len > 8:
        return four_to_hanstr(num_str[:-8]) + "亿" + four_to_hanstr(num_str[-8: -4]) + "万" + four_to_hanstr(
            num_str[-4:]) + "圆"
    elif str_len > 4:
        return four_to_hanstr(num_str[: -4]) + "万" + four_to_hanstr(num_str[-4:]) + "圆"
    else:
        return four_to_hanstr(num_str) + "圆"


def decimal_to_str(num_str: str):
    result = ""
    num_len = len(num_str)
    if num_len > 2:
        print("输入的金额不合法")
        return
    if num_str == "0" or num_str == "00":
        return "整"
    # 理论只有两位
    i = int(num_str[0])
    result += han_list[i] + decimal_unit_list[0]
    if num_len > 1:
        i = int(num_str[1])
        result += han_list[i] + decimal_unit_list[1]
    return result


if __name__ == '__main__':
    num = float(input("请输入金额\n"))
    integer, fraction = divide(num)
    print(integer_to_str(integer) + decimal_to_str(fraction))
