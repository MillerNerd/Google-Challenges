def lambs(total_lambs):
    return stingy(total_lambs) - generous(total_lambs)


def generous(total_lambs):
    if total_lambs < 3:
        return 1
    # c = 1
    # iterator
    n = 1
    while 2 ** n <= (total_lambs + 1):
        n = n + 1
    return n - 1


def stingy(total_lambs):
    if total_lambs < 2:
        return 1
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
