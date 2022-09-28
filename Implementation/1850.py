A, B = map(int, input().split())

def gcd(a, b):
    if a % b:
        return gcd(b, a%b)

    return b


print('1' * gcd(max(A, B), min(A, B)))

