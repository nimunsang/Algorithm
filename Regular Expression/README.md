# REGULAR EXPRESSION

### 문자 클래스 ( [ ] )

[ ] 사이의 문자들과 매치   
ex) [abc] : a, b, c중 한개의 문자와 매치   
* [0-9] : 숫자   
* [a-zA-z] : 알파벳 모두   
* [^0-9] : 숫자가 아닌 문자
* `\d` : 숫자와 매치 ( `[0-9]` )   
* `\D` : 숫자가 아닌 것과 매치 ( `[^0-9]` )   
* `\s` : 공백문자와 매치
* `\S` : 공백문자가 아닌 것과 매치
* `\w` : 문자+숫자와 매치 ( `[a-zA-Z0-9_]` )
* `\W` : 문자+숫자가 아닌 것과 매치 ( `[^a-zA-Z0-9_]` )

---

### Dot( . )

줄바꿈 문자인 `\n`을 제외한 모든 문자와 매치   
ex) `a.b` : a + 모든문자 + b 
* "aab" : 매치
* "a0b" : 매치
* "abc" : 매치x
* `a[.]b` 와 `a.b` 는 다르다   
* `a[.]b`는 "a.b"와 매치, "a0b"와 매치x

---

### 반복( { } , * , + )

* '{m}' : 반복횟수가 반드시 m
* '{m, n}' : 반복횟수가 m부터 n까지 매치        
* '*' : 0개 이상 반복 ( `{0,}` )    
* '+' : 1개 이상 반복 ( `{1,}` )    
* '?' : 있어도 되고, 없어도 된다 ( `{0,1}` )    
ex) ca{2}t : caat     
ex) ca{2,5}t : caat, caaat, caaaat, caaaaat

---

### [골드5] #1013 (https://www.acmicpc.net/problem/1013)

> 특정한 패턴이 주어졌을 때, 문자열이 패턴에 일치하는지 검사하는 문제이다.
> 
* **문제 해결 알고리즘 : ```정규표현식```**

`re.fullmatch()` 를 사용하면, 바로 풀리는 문제이다.

---

### [실버3] #9996 (https://www.acmicpc.net/problem/9996)

> 특정한 패턴이 주어졌을 때, 그 패턴과 일치하는 문자열을 찾는 문제이다.

* **문제 해결 알고리즘 : ```정규표현식```**

COMMENT : `^` , `$` 는 각각, 시작, 끝에 와야만 하는 것을 매치한다.

---

### [실버4] #5637 (https://www.acmicpc.net/problem/5637)

> 주어진 문장에서, 알파벳과 하이픈으로만 이루어진 단어 중 가장 길이가 긴 단어를 찾는 문제이다.

* **문제 해결 알고리즘 : ```정규표현식```**

`re.findall(regex, string)` 을 이용하여, 해결 가능했다.    
regex는, `r'[a-zA-Z-]+'` 로 구성했다.

---

### [실버5] #14405 (https://www.acmicpc.net/problem/14405)

> 문자열을, 주어진 문자열로만으로 표현할 수 있는가 묻는 문제이다.

* **문제 해결 알고리즘 : ```정규표현식```**

`re.sub(regex, 치환할문자열, string)` 을 이용하여, 해결 가능했다.   
regex는, `r'문자열|문자열|문자열'` 로 구성했다.

---

### [브론즈1] #3447 (https://www.acmicpc.net/problem/3447)

> 주어진 문자열에서 특정한 단어 ('BUG') 를 반복해서 지우는 문제이다.

* **문제 해결 알고리즘 : ```정규표현식```**

`re.sub(regex, 치환할문자열, string)` 을 이용하여, 쉽게 해결 가능한 문제였다.

---




