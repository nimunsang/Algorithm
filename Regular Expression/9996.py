import re

N = int(input())

pattern = input().rstrip()
pattern = pattern.replace('*', '[a-z]*')
pattern = '^' + pattern + '$'
for _ in range(N):
    S = input().rstrip()
    print("DA" if re.findall(pattern, S) else "NE")
