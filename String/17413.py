S = input()


def make_reverse_string(s):
    lst = list(s.split())
    return ' '.join(list(map(lambda x: x[::-1], lst)))


answer = ""
target = ""
istag = 0
for a in S:
    if a == '<':
        answer += make_reverse_string(target)
        target = ""
        istag = 1
        answer += '<'
        continue
    elif a == '>':
        istag = 0
        answer += '>'
        continue

    if istag:
        answer += a
    else:
        target += a

if target:
    answer += make_reverse_string(target)

print(answer)



