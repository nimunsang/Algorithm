N, L = map(int, input().split())
lst = sorted(list(map(int, input().split())))

answer = 0

tmp = 0
for i in range(N):
    if tmp < lst[i] + 0.5:
        tmp = lst[i] + L - 0.5
        answer += 1

print(answer)