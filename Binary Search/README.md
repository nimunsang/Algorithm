# Binary Search

- ### 정렬되어 있는 배열에서, 탐색 범위를 반으로 줄이며 특정한 값을 찾아내는 알고리즘

- ### 시간 복잡도 : O(log N)

1. 배열의 가운데에 위치한 임의의 값을 선택한다.

2. 값이 찾는 값보다 작다면, 임의의 값을 기준으로 왼쪽에 있는 배열 값들을 대상으로 1. 을 진행한다.   
값이 찾는 값보다 크다면, 임의의 값을 기준으로 오른쪽에 있는 배열 값들을 대상으로 1. 을 진행한다.   
원하는 값을 찾았다면, 탐색을 종료한다.

3. 값을 찾거나, 간격이 비어있을 때까지 반복한다.    
   종료 조건 1: 검색을 성공할 경우 (array[mid] == key)     
   종료 조건 2: 검색을 실패할 경우 (low > high)

- ### 주의할 점
  - 정렬된 배열에서만 사용 가능하다.
  - 이분 탐색을 사용하는 문제는 대부분 수의 범위가 크기 때문에, 오버플로우에 주의해야 한다.
  - 탈출 조건 처리를 할 때, (low + 1 < high , low < high, low <= high) 각각의 방법들에 대해,    
  무한 루프에 빠지지 않도록 탈출 조건을 잘 설계해야 한다. 
  - 문제의 **upper bound**를 묻는 문제인지, **lower bound**인지 잘 파악해야 한다.
  - low, high의 범위와, low를 return 할지, high를 return 할지를 잘 생각해 주어야 한다. 

- ### 구현
```
def BinarySearch(array, value, low, high):
    while low + 1 < high:
        mid = (low + high) // 2
        if array[mid] <= value:
            low = mid
        else:
            high = mid
    return low
```


- ### Lower Bound
    - 찾고자 하는 값보다 크거나 같은 값이 처음 나타나는 위치

```
def LowerBound(array, value, low, high):
    while low + 1 < high:
        mid = (low + high) // 2
        if array[mid] < value:
            low = mid
        else:
            high = mid
    return high
```
- ### Upper Bound
    - 찾고자 하는 값보다 큰 값이 처음 나타나는 위치    
```
def UpperBound(array, value, low, high):
    while low + 1 < high:
        mid = (low + high) // 2
        if array[mid] <= value:
            low = mid
        else:
            high = mid
    return high
```


-----
<br>

## 문제

---

### [실버2] #2792 (https://www.acmicpc.net/problem/2792)

> 매개 변수 탐색 문제이다. 

* **문제 해결 알고리즘 : ```이분 탐색```**

**주의할 점 : low, high의 범위와, RETURN값을 무엇으로 할지 잘 생각해야 한다.**

---

---

### [실버4] #2417 (https://www.acmicpc.net/problem/2417)

> 정수가 주어질 때, 그 수의 정수 제곱근을 구하는 문제이다. 단, 범위가 매우 크다.

* **문제 해결 알고리즘 : ```이분 탐색```**

**주의할 점 : low, high의 범위와, RETURN값을 무엇으로 할지 잘 생각해야 한다.**

---