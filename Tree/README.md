# Tree

## Minimum Spanning Tree

* ### Spanning Tree ?

  * 그래프의 모든 노드가 연결되어 있고, 트리의 속성을 만족(사이클 존재 x)하는 그래프

* ### Mimimum Spanning Tree (MST) ?

  * 가능한 Spanning Tree 중에서, 간선의 가중치의 합이 최소인 Spanning Tree
  * Kruskal Algorithm
  * Prim Algorithm

* ### Kruskal Algorithm

  * **Greedy Algorithm**과, **Union-Find Algorithm**을 기초로 함
  * O(ElogE)

  * #### 구현
    1. 모든 정점을 독립적인 집합으로 만든다.
    2. 모든 간선을 비용을 기준으로 정렬하고, 비용이 적은 간선부터 양 끝의 두 정점을 비교한다.
    3. 두 정점의 최상위 정점을 비교하고, 서로 다를 경우 두 정점을 연결한다.
       * MST는 사이클이 없으므로, 사이클이 생기지 않도록 하는 것

  
  ```python
    def kruskal(graph):
        mst = list()
        
        for edge in edges:
            weight, node_v, node_next_v = edge
            if find(node_v) != find(node_next_v):
                union(node_v, node_next_v)
                mst.append(edge)
        
        return mst
  ```

* ### Prim Algorithm

  * 시작 정점을 선택한 후, 정점에 인접한 간선 중 최소 간선으로 연결된 정점을 선택
  * 해당 정점에서 다시 최소 간선으로 연결된 정점을 선택하는 방식
  * O(ElogE)
  * #### 구현
    1. 임의의 정점을 선택, '연결된 노드 집합'에 삽입
    2. 선택된 정점에 연결된 간선들을 간선 리스트에 삽입
    3. 간선 리스트에서 최소 가중치를 가지는 간선부터 추출해서,    
       c-1. 해당 간선에 연결된 인접 정점이 '연결된 노드 집합'에 이미 들어있다면, 스킵 (Cycle 발생)    
       c-2. 해당 간선에 연결된 인접 정점이 '연결된 노드 집합'에 들어있지 않다면, 해당 간선을 선택하고, 해당 간선 정보를 '최소 신장 트리'에 삽입
    4. 추출한 간선은 간선 리스트에서 제거
    5. 간선 리스트에 더 이상의 간선이 없을 때 까지 c~d를 반복


* ### Prim vs Kruskal
  * 두 알고리즘 모두, Greedy Algorithm을 기초로 한다.
  * Kruskal은 가장 가중치가 작은 간선부터 선택하면서 MST를 구함 (정렬 우선)
  * Prim은 특정 정점에서 시작, 해당 정점에 연결된 가장 가중치가 작은 간선을 선택 (heap 사용)


---

### [골드4] #4386 (https://www.acmicpc.net/problem/4386)

> 좌표 평면 위의 점들이 주어질 때, 점들을 모두 잇는 길이들의 합 중 최솟값을 구하는 문제이다.

* **문제 해결 알고리즘 : ```Kruskal```, ```Prim```**

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

