def solution(n):
    # Google's inputs are strings, not ints
    n = int(n)
    count = 0
    while n > 1:
        # n == 3 is a special case
        # all other odd #s benefit from adding/subbing to the nearest divisible by 4
        # 3 can just be sub'd twice
        if n == 3:
            return count + 2
        # if even, half
        # this will always reduce more than -1
        # except for 2, which would be the same
        if n % 2 == 0:
            count = count + 1
            n = n / 2
        # if odd, go to nearest divisible by 4
        # have to either add or sub anyways
        # might as well set up for 2 divisions
        else:
            if (n + 1) % 4 == 0:
                n = n + 1
                count = count + 1
            else:
                n = n - 1
                count = count + 1
    return count
