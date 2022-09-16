from math import *
import sys
input = sys.stdin.readline


def init_min(start, end, index):
    if start == end:
        tree_min[index] = arr[start]

    else:
        mid = (start + end) // 2
        tree_min[index] = min(init_min(start, mid, index * 2), init_min(mid + 1, end, index * 2 + 1))

    return tree_min[index]


def init_max(start, end, index):
    if start == end:
        tree_max[index] = arr[start]

    else:
        mid = (start + end) // 2
        tree_max[index] = max(init_max(start, mid, index * 2), init_max(mid + 1, end, index * 2 + 1))
    return tree_max[index]


def find_min(start, end, index, left, right):
    if left > end or right < start:
        return sys.maxsize

    if start >= left and end <= right:
        return tree_min[index]

    mid = (start + end) // 2
    return min(find_min(start, mid, index * 2, left, right), find_min(mid + 1, end, index * 2 + 1, left, right))


def find_max(start, end, index, left, right):
    if left > end or right < start:
        return 0

    if start >= left and end <= right:
        return tree_max[index]

    mid = (start + end) // 2
    return max(find_max(start, mid, index * 2, left, right), find_max(mid + 1, end, index * 2 + 1, left, right))

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
h = int(ceil(log2(N)))
tree_min = [0] * (2**(h+1))
tree_max = [0] * (2**(h+1))
init_min(0, N-1, 1)
init_max(0, N-1, 1)

for _ in range(M):
    a, b = map(int, input().split())
    print(find_min(0, N-1, 1, a-1, b-1), find_max(0, N-1, 1, a-1, b-1))