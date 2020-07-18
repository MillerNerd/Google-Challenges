def solution(num):
    count = 0
    while num > 1:
        if num == 3:
            return count + 2
        # if even, half
        if num % 2 == 0:
            count = count + 1
            num = num / 2
        else:
            # nearest num divisible by 4 is most efficient
            # this isn't true for 3
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