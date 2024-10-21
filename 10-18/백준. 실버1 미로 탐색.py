import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

q = deque()
q.append((0, 0, 1))
v = [[0] * m for _ in range(n)]
di = [(0, 1), (0, -1), (1, 0), (-1, 0)]
v[0][0] = 1
while q:
    y, x, move = q.popleft()

    if y == n-1 and x == m-1:
        print(move)
        break

    for d in di:
        dy = y + d[0]
        dx = x + d[1]
        if dy < 0 or dy >= n or dx < 0 or dx >= m:
            continue
        if not v[dy][dx] and arr[dy][dx]:
            v[dy][dx] = 1
            q.append((dy, dx, move+1))
