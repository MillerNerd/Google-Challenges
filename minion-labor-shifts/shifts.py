import collections


def solution(data, n):
    repeats = collections.Counter(data)
    return [i for i in data if repeats[i] <= n]
