def solution(n):
    n = int(n)
    count = 0
    while n > 1:
        if n == 3:
            return count + 2
        # if even, half
        if n % 2 == 0:
            count = count + 1
            n = n / 2
        else:
            # nearest num divisible by 4 is most efficient
            # this isn't true for 3
            n = round(n/4.0)
            count = count + 3
    return count


# def even(num):
#     if num == 1:
#         return
#
#
# def odd(num):
#     pass
