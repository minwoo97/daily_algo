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

