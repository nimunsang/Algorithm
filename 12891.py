import sys
input = sys.stdin.readline

S, P = map(int, input().split())
dna = input().rstrip()
cnt = list(map(int, input().split()))
mask = ['A', 'C', 'G', 'T']
dic = {mask[i] : cnt[i] for i in range(4)}

def check():
    for value in dic.values():
        if value > 0:
            return False
    return True


for i in range(P):
    dic[dna[i]] -= 1

answer = 0
if check():
    answer += 1

for i in range(S-P):
    dic[dna[i]] += 1
    dic[dna[i+P]] -= 1
    if check():
        answer += 1

print(answer)


