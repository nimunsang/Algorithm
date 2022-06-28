import re

regex = r'BUG'

while True:
    try :
        s = input().rstrip()
    except :
        break

    a = re.sub(regex, "", s)
    while a != re.sub(regex, "", a):
        a = re.sub(regex, "", a)
    print(a)
