import math


def solution(x, y):
    x = int(x)
    y = int(y)
    if x < 0 > y:
        return "impossible"
    count = 0
    if x == 1 == y:
        return count
    print(x, y, count)
    while x > 1 or y > 1:
        if x == y:
            return "impossible"
        if (x % 2) == 0 == (y % 2):
            return "impossible"
        # if x % y == 0 or y % x == 0:
        #     return "impossible 3"
        if y > x:
            steps = math.ceil((y-x)/x)
            count = count + steps
            y = y - steps * x
            # y = y - x
            # count = count + 1
        if x > y:
            steps = math.ceil((x-y)/y)
            count = count + steps
            x = x - steps * y
            # x = x - y
            # count = count + 1
    return count
