import math


def lambs(total_lambs):
    return stingy(total_lambs) - generous(total_lambs)


def generous(total_lambs):
    # sum of 2^(0-N) is 2^(N+1)-1
    # solve for N using log
    return int(math.log(total_lambs+1, 2))


def stingy(total_lambs):
    if total_lambs < 2:
        return 1
    # failed attempt at removing iteration
    # the sum of fib(0:N) happens to be fib(n+2)-1
    # https://www.geeksforgeeks.org/find-index-given-fibonacci-number-constant-time/
    # return math.floor(2.078087 * math.log(total_lambs + 1) + 1.672276) - 2

    # instead, iterate through fib until fib(n) > total_lambs+1

    # fib - 2
    a = 0
    # fib - 1
    b = 1
    # fib
    c = 1
    # N/iterator
    n = 1
    while c <= (total_lambs + 1):
        # fib(n)
        c = a + b
        # iterate
        n = n + 1
        a = b
        b = c
    return n - 3
