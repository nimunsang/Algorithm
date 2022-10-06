import sys
input = sys.stdin.readline


dic = dict()
N = int(input())
for _ in range(N):
    s = input().rstrip().split('.')[1]
    dic[s] = dic.get(s, 0) + 1

for k, v in sorted(dic.items()):
    print(k, v)
