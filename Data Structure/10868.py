import sys
from math import *
input = sys.stdin.readline


def init(start, end, index):
    if start == end:
        tree[index] = A[start]
    else:
        mid = (start + end) // 2
        tree[index] = min(init(start, mid, index * 2), init(mid + 1, end, index * 2 + 1))
    return tree[index]


def find_min(start, end, index, left, right):
    if left > end or right < start:
        return sys.maxsize

    if start >= left and end <= right:
        return tree[index]

    mid = (start + end) // 2
    return min(find_min(start, mid, index * 2, left, right), find_min(mid + 1, end, index * 2 + 1, left, right))


N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
height = int(ceil(log2(N)))
tree = [0] * 2**(height+1)
init(0, N-1, 1)
for _ in range(M):
    a, b = map(int, input().split())
    print(find_min(0, N-1, 1, a-1, b-1))