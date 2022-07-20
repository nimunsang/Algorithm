import sys
input = sys.stdin.readline


N = int(input())
lst = list(map(int, input().split()))
X = int(input())

lst.sort()
start, end = 0, N-1

answer = 0
while start < end:
    if lst[start] + lst[end] == X:
        answer += 1
        start += 1
    elif lst[start] + lst[end] > X:
        end -= 1
    else:
        start += 1

print(answer)