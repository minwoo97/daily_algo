# 10월 18일

### 제목
```
```

# 10월 17일

### DFS와 BFS
```
import sys
from collections import deque
input = sys.stdin.readline

n, m, start = map(int, input().split())

lst = [[] for _ in range(n + 1)]
v = [0 for _ in range(n + 1)]

# 양방향으로 방문 가능하니까 둘다 추가
for _ in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

# 리스트의 정렬이 필요함 낮은거를 우선으로 방문해서
for i in lst:
    i.sort()


def dfs(num):
    print(num, end=' ')
    for i in lst[num]:
        if not v[i]:
            v[i] = 1
            dfs(i)
            
# 재귀로 해결하기 넣기 전에 방문 처리 해주고 dfs 시작
v[start] = 1
dfs(start)
print()


#여기서부터는 bfs시작

v = [0 for _ in range(n + 1)]
q = deque()
q.append(start)
v[start] = 1

# 잘보면 dfs랑 bfs 생긴게 비슷하다?
while q:
    num = q.popleft()
    print(num, end=' ')
    for j in lst[num]:
        if not v[j]:
            v[j]=1
            q.append(j)
            
print()
```

# 10월 16일

### n과 m(2)
```
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
v = [0 for _ in range(n+1)]

def dfs(lst, last):
    if len(lst) == m:
        print(*lst)
        return

    for i in range(1, n+1):
        if not v[i] and i > last:
            v[i] = 1
            lst.append(i)
            dfs(lst, i)
            lst.pop()
            v[i] = 0
dfs([], 0)
```

### n과 m(4)
```
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def dfs(lst, last):
    if len(lst) == m:
        print(*lst)
        return

    for i in range(1, n+1):
        if i >= last:
            lst.append(i)
            dfs(lst, i)
            lst.pop()
dfs([], 0)
```

### n과 m(5)
```
import sys

def dfs(tlst):
    if len(tlst) == m:
        print(*tlst)
        return

    for i in lst:
        if not v[i]:
            v[i] = 1
            tlst.append(i)
            dfs(tlst)
            tlst.pop()
            v[i] = 0


input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
v = [0] * (max(lst) + 1)

for i in lst:
    if not v[i]:
        v[i] = 1
        dfs([i])
        v[i] = 0
```

### 헌내기는 친구가 필요해
```
from collections import deque
n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

#n은 세로 m은 가로

doyeon = ()
p = []
v = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            doyeon = (i, j)
        elif arr[i][j] == 'P':
            p.append((i, j))

di = [(0, 1), (-1, 0), (0, -1), (1, 0)]

ans = 0
q = deque([doyeon])

v[doyeon[0]][doyeon[1]] = 1
while q:
    y, x = q.popleft()
    if arr[y][x] == 'P':
        ans += 1
    kand = v
    for d in di:
        dy = y + d[0]
        dx = x + d[1]
        if not (0<=dy<n and 0<=dx<m):
            continue
        if not v[dy][dx] and not arr[dy][dx] == 'X':
            v[dy][dx] = 1
            q.append((dy, dx))

if not ans:
    print('TT')
else:
    print(ans)
```
