import re

# (100+1+ | 01)+

regex = r'(100+1+|01)+'
T = int(input())
for _ in range(T):
    S = input().rstrip()
    print("YES" if re.fullmatch(regex, S) else "NO")