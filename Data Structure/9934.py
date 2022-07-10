N = int(input())
lst = list(map(int, input().split()))


answer = [[] for _ in range(N)]
def solve(center, dist, height):
    if dist == 0:
        return

    answer[height].append(lst[center])

    solve(center-dist//2, dist//2, height+1)
    solve(center+dist//2, dist//2, height+1)


d = 2**(N-1)
solve(d-1, d, 0)
for a in answer:
    print(*a)