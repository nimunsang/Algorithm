N, K = map(int, input().split())
lst = list(map(int, input().split()))

answer = sum(lst[:K])
for i in range(N-K+1):
    answer = max(answer, sum(lst[i:i+K]))

print(answer)