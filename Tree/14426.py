from bisect import bisect_left
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [input().rstrip() for _ in range(N)]
lst.sort()


answer = 0
for _ in range(M):
    s = input().rstrip()
    idx = bisect_left(lst, s)
    if idx < N and lst[idx][:len(s)] == s:
        answer += 1

print(answer)


# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# allset = set()
#
# for _ in range(N):
#     a = input().rstrip()
#     for i in range(1, len(a)+1):
#         allset.add(a[:i])
#
#
# answer = 0
# for _ in range(M):
#     s = input().rstrip()
#     if s in allset:
#         answer += 1
#
# print(answer)