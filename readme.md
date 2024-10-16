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