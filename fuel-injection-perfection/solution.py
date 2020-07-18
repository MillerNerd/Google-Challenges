def solution(num):
    count = 0
    while num > 1:
        # if even, half
        if num % 2 == 0:
            count = count + 1
            num = num / 2
        else:
            if (num + 1) % 4 == 0:
                num = num + 1
                count = count + 1
            else:
                num = num - 1
                count = count + 1
    return count


# def even(num):
#     if num == 1:
#         return
#
#
# def odd(num):
#     pass