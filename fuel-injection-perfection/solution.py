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
        # if odd, go to nearest divisible by 4
        else:
            if (n + 1) % 4 == 0:
                n = n + 1
                count = count + 1
            else:
                n = n - 1
                count = count + 1
    return count
