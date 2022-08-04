N, M = map(int, input().split())
lst = list(map(int, input().split()))


subtotal = sum(lst[:M])
answer = subtotal
for i in range(N-M):
    subtotal = subtotal - lst[i] + lst[i+M]
    answer = max(answer, subtotal)

print(answer)