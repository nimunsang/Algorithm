from collections import Counter

S = list(input())
L = len(S)
counter = Counter(S)

odd = 0
for key, value in counter.items():
    if value % 2 == 1:
        odd += 1

if (L % 2 == 0 and odd > 0) or (L % 2 == 1 and odd != 1):
    print("I'm Sorry Hansoo")

else:
    answer = ""
    if L%2 == 0:
        for key, value in sorted(counter.items(), key = lambda x: x[0]):
            for i in range(value // 2):
                answer += key
        answer += answer[::-1]

    else:
        piv = ""
        for key, value in sorted(counter.items(), key= lambda x: x[0]):
            for i in range(value // 2):
                answer += key

            if value % 2 == 1:
                piv = key

        answer += piv
        answer += answer[:-1][::-1]

    print(answer)
