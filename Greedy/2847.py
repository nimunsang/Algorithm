N = int(input())
lst = [int(input()) for _ in range(N)]

answer = 0
for i in range(N-1, 0, -1):
    while lst[i-1] >= lst[i]:
        lst[i-1] -= 1
        answer += 1

print(answer)