from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    W = input().rstrip()
    K = int(input())
    dic = defaultdict(list)

    for i in range(len(W)):
        if W.count(W[i]) >= K:
            dic[W[i]].append(i)

    if not dic:
        print(-1)
        continue

    ans1, ans2 = float('inf'), 0
    for lst in dic.values():
        for i in range(0, len(lst)-K+1):
            ans1 = min(ans1, lst[K+i-1] - lst[i])
            ans2 = max(ans2, lst[K+i-1] - lst[i])

    print(ans1+1, ans2+1)