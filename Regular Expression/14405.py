import re

S = input()
regex = r'pi|ka|chu'
print("NO" if re.sub(regex, "", S) else "YES")