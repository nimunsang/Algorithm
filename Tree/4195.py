from collections import defaultdict
import sys
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    roota = find(a)
    rootb = find(b)

    if roota < rootb:
        parent[rootb] = roota
        cnt[roota] += cnt[rootb]

    else:
        parent[roota] = rootb
        cnt[rootb] += cnt[roota]


T = int(input())
for _ in range(T):
    F = int(input())
    dic = defaultdict(int)
    parent = [i for i in range(2*F+1)]
    cnt = [1 for i in range(2*F+1)]
    idx = 0
    for __ in range(F):
        A, B = input().rstrip().split()
        if A not in dic:
            dic[A] = idx
            idx += 1

        if B not in dic:
            dic[B] = idx
            idx += 1

        a, b = dic[A], dic[B]

        if find(a) != find(b):
            union(a, b)

        print(cnt[find(a)])
