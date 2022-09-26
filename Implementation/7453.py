from collections import defaultdict
import sys
input = sys.stdin.readline


N = int(input())
inp = [list(map(int, input().split())) for _ in range(N)]
A, B, C, D = [], [], [], []
for i in range(N):
    for j in range(4):
        v = inp[i][j]
        if j == 0:
            A.append(v)
        elif j == 1:
            B.append(v)
        elif j == 2:
            C.append(v)
        else:
            D.append(v)

dic = dict()

for a in A:
    for b in B:
        dic[a+b] = dic.get(a+b, 0) + 1

answer = 0

for c in C:
    for d in D:
        answer += dic.get(-(c+d), 0)

print(answer)