import sys

N, M = map(int, input().split())
S = set([sys.stdin.readline().rstrip() for _ in range(N)])
targets = [sys.stdin.readline().rstrip() for _ in range(M)]

answer = 0
for target in targets:
    if target in S:
        answer += 1
print(answer)



# import sys
#
# sys.setrecursionlimit(10**6)
#
# N, M = map(int, input().split())
# S = [sys.stdin.readline().rstrip() for _ in range(N)]
# targets = [sys.stdin.readline().rstrip() for _ in range(M)]
# S.sort()
# targets.sort()
# S_length = len(S)
#
#
# def binary_search(start, end, target):
#     global is_include
#
#     if start >= end:
#         if target != S[end]:
#             is_include = 0
#         return
#
#     mid = (start+end)//2
#
#     if S[mid] == target:
#         return
#
#     elif S[mid] > target:
#         binary_search(start, end-1, target)
#     else:
#         binary_search(mid+1, end, target)
#
#
# answer = 0
# for target in targets:
#     is_include = 1
#     binary_search(0, S_length-1, target)
#     if is_include:
#         answer += 1
# print(answer)
