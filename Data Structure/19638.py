import heapq
import sys
input = sys.stdin.readline

# 1 <= N <= 10^5 || 1 <= H <= 2*10^9 || 1 <= T <= 10^5
N, H, T = map(int, input().split())
lst = [-int(input()) for _ in range(N)]

# O(N)
heapq.heapify(lst)

cnt = 0

# O(T) * 2 * O(logN) ==> O(TlogN) ==> O(10^5 * 20)
for _ in range(T):
    if -lst[0] == 1 or -lst[0] < H:
        break
    a = heapq.heappop(lst)
    heapq.heappush(lst, -((-a)//2))
    cnt += 1

if -lst[0] < H:
    print("YES")
    print(cnt)
else:
    print("NO")
    print(-lst[0])
