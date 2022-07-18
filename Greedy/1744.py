N = int(input())
lst = [int(input()) for _ in range(N)]

pos = []
neg = []
zero = 0

for num in lst:
    if num < 0:
        neg.append(num)
    elif num > 0:
        pos.append(num)
    else:
        zero += 1


answer = 0

pos.sort(reverse=True)

if len(pos) % 2 == 0:
    for i in range(0, len(pos), 2):
        answer += max(pos[i] * pos[i+1], pos[i] + pos[i+1])
else:
    for i in range(0, len(pos)-1, 2):
        answer += max(pos[i] * pos[i+1], pos[i] + pos[i+1])
    answer += pos[-1]

neg.sort()
if len(neg) % 2 == 1:
    if zero:
        neg.pop()
    else:
        neg.append(1)

for i in range(0, len(neg), 2):
    answer += neg[i] * neg[i+1]

print(answer)