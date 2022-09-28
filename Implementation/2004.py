N, M = map(int, input().split())

def cnt(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count


print(min(cnt(N, 5) - cnt(N-M, 5) - cnt(M, 5), cnt(N, 2) - cnt(N-M, 2) - cnt(M, 2)))