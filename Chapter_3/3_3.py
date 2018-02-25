# @Author: Libukai
# @Date:   2018-02-22 03:01:58
# @Last modified by:   likai
# @Last modified time: 2018-02-25 04:04:17


def symbol(row, line):
    if row % 5 == 0 and line % 5 != 0:
        symbol = '-'
    elif row % 5 != 0 and line % 5 == 0:
        symbol = '|'
    elif row % 5 == 0 and line % 5 == 0:
        symbol = '+'
    else:
        symbol = ' '
    return symbol


def squre(num):
    squre_num = (num - 1) * 5 + 1
    for row in range(squre_num):
        line_symbol = ''
        for line in range(squre_num):
            line_symbol += symbol(row, line)
        print(line_symbol)


if __name__ == '__main__':
    num = int(input('请输入表格的大小:'))
    squre(num)
