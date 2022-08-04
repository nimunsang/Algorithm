import sys
input = sys.stdin.readline


N, X = map(int, input().split())
lst = list(map(int, input().split()))

subtotal = sum(lst[:X])
answer = subtotal
cnt = 1
for i in range(N-X):
    subtotal = subtotal - lst[i] + lst[i+X]
    if subtotal > answer:
        answer = subtotal
        cnt = 1
    elif subtotal == answer:
        cnt += 1


if answer == 0:
    print("SAD")
else:
    print(answer)
    print(cnt)