N = input()
tmp = answer = 0
for i in range(1, len(N)):
    tmp = i*(10**i - 10**(i-1))
    answer += tmp

answer += len(N) * (int(N)-(10**(len(N)-1)-1))
print(answer)