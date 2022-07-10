N = int(input())

dic = dict()
lst = []
for _ in range(N):
    S = input()
    lst.append(S)
    for i in range(len(S)):
        char = S[i]
        if char not in dic:
            dic[char] = 10**(len(S)-i)
        else:
            dic[char] += 10**(len(S)-i)

sorted_dic = sorted(dic.items(), key= lambda x: -x[1])

dic = dict()
num = 9
for key, value in sorted_dic:
    dic[key] = str(num)
    num -= 1

answer = 0
for string in lst:
    for i in range(len(string)):
        char = string[i]
        answer += int(dic[char]) * 10**(len(string)-(i+1))

print(answer)

