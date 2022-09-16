import sys
input = sys.stdin.readline


def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
    else:
        mid = (start + end) // 2
        tree[index] = min(init(start, mid, index * 2), init(mid + 1, end, index * 2 + 1))
    return tree[index]


def update(start, end, index, w, v):
    if w < start or w > end:
        return

    if start == end:
        tree[index] = v
        return tree[index]

    mid = (start + end) // 2
    update(start, mid, index * 2, w, v)
    update(mid + 1, end, index * 2 + 1, w, v)
    tree[index] = min(tree[index * 2], tree[index * 2 + 1])



def find_min(start, end, index, left, right):
    if start > right or end < left:
        return [sys.maxsize, sys.maxsize]

    if start >= left and end <= right:
        return tree[index]

    mid = (start + end) // 2
    return min(find_min(start, mid, index * 2, left, right), find_min(mid + 1, end, index * 2 + 1, left, right))


N = int(input())
A = list(map(int, input().split()))
arr = [[v, i] for i, v in enumerate(A, 1)]

tree = [0] * (N*4)
init(0, N-1, 1)

print(tree)
M = int(input())
for _ in range(M):
    Q = list(map(int, input().split()))
    cmd = Q[0]
    if cmd == 1:
        i, v = Q[1], Q[2]
        arr[i-1][0] = Q[2]
        update(0, N-1, 1, i-1, arr[i-1])

    elif cmd == 2:
        print(find_min(0, N-1, 1, 0, N-1)[1])
