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