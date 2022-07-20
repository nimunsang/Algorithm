import sys
input = sys.stdin.readline

N, M = map(int, input().split())
known = set(input().split()[1:])
partys = [set(input().split()[1:]) for _ in range(M)]

for _ in range(M):
    for party in partys:
        if known & party:
            known = known.union(party)

answer = 0
for party in partys:
    if known & party:
       continue
    answer += 1

print(answer)
