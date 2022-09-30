S = input()

def check_palindrome(s):
    s = '#' + '#'.join(list(s)) + '#'
    center = len(s)//2
    for i in range(len(s)//2 + 1):
        if s[center - i] != s[center + i]:
            return 0

    return 1


idx = 0
for i in range(len(S)):
    if check_palindrome(S[i:]):
        idx = i
        break

print(len(S) + idx)