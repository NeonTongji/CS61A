
def mario_number(level):
    def double(level, num):
        sum_num = 0
        while level:
            if level % 100 == num:
                sum_num, level = sum_num + 1, level // 100
            else:
                level = level // 10
        return sum_num
    if double(level, 0) != 0:
        return 0
    else:
        return double(level, 11) + 1 

