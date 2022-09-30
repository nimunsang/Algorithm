S = '#'+'#'.join(list(input()))+'#'
print("true" if S[:len(S)//2] == S[len(S)//2+1:][::-1] else "false")