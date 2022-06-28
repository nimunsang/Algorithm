import re

regex = r'[a-zA-Z-]+'
answer = ""
end = 0
while end == 0:
    line = input().rstrip()
    if line:
        if 'E-N-D' in line:
            line = line.replace('E-N-D', "")
            end = 1
        maxline = max(re.findall(regex, line), key=len)
        if len(maxline) > len(answer):
            answer = maxline

print(answer.lower())