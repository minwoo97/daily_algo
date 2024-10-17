import sys
from collections import deque
input = sys.stdin.readline

n, m, start = map(int, input().split())

lst = [[] for _ in range(n + 1)]
v = [0 for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

# 리스트의 정렬이 필요함 낮은거를 우선으로 방문해서
for i in lst:
    i.sort()

v[start] = 1
def dfs(num):
    print(num, end=' ')
    for i in lst[num]:
        if not v[i]:
            v[i] = 1
            dfs(i)

dfs(start)
print()

v = [0 for _ in range(n + 1)]
q = deque()
q.append(start)
v[start] = 1
while q:
    num = q.popleft()
    print(num, end=' ')
    for j in lst[num]:
        if not v[j]:
            v[j]=1
            q.append(j)
print()

