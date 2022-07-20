# Tree



---

### [실버1] #15900 (https://www.acmicpc.net/problem/15900)

> 트리가 주어질 때, 트리의 리프노드들로부터 루트노드 까지의 거리의 합을 구하는 문제이다.

* **문제 해결 알고리즘 : ```DFS```**

---

### [실버2] #14426 (https://www.acmicpc.net/problem/14426)

> 문자열들로 이루어진 리스트에서, input으로 주어진 문자열이 리스트 안의 문자열의 접두사들 중 같은 것이 있는지 판별하는 문제이다.

* **문제 해결 알고리즘 : ```집합```, ```이분 탐색```**


* 문제 인식
  * 시간제한 1초
  * 문자열들의 최대 길이 : 100(S)
  * 리스트의 최대 크기 : 10000(N)
  * input으로 주어지는 문자열의 개수 : 10000(M)
  

* 내가 푼 처음 풀이
  * 리스트의 접두사들로 이루어진 집합을 만든다 (최대 집합 크기 : 100*10000) -> O(S(S-1)/2 * N)
  * input in set 을 이용 -> M * O(1) -> O(M)
  * 즉, O(S^2 * N)에 해결 가능


* 이분 탐색을 이용한 풀이
  * 리스트를 정렬 -> O(NlogN)
  * input을 리스트에서 이분탐색(lower bound) -> O(logN)
  * input과 리스트 idx값 일치하는가 확인 -> O(S)
  * 즉, O(NlogN) + O(S*logN)에 해결 가능


* 결론
  * 이분 탐색을 이용한 풀이가 훨씬 빠르다.
  * python에서의 **from bisect import bisect_left**를 적극 활용하자.

---
