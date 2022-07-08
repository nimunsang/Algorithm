import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

subtotal = sum(lst[:K])
answer = subtotal
for i in range(N-K):
    subtotal -= lst[i]
    subtotal += lst[i+K]
    answer = max(answer, subtotal)

print(answer)
