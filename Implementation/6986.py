import sys
import decimal

input = sys.stdin.readline
N, K = map(int, input().split())
lst = [(float(input().rstrip())) for _ in range(N)]
lst.sort()
lst = list(map(str, lst))
epsilon = 1e-9

cut = lst[K:N-K]
lst2 = [lst[K]] * K + lst[K:N-K] + [lst[N-K-1]] * K

def calc(lst, n):
    total = sum([decimal.Decimal(num) for num in lst])
    ave = round(total / n + decimal.Decimal(str(epsilon)) , 2)
    return ave


print(calc(cut, N-2*K))
print(calc(lst2, N))
