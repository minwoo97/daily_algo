def dfs(a, b):
    global ans
    now = 0
    cnt = 0
    bwlst = ['W', 'B']
    if arr[a][b] == 'W':
        now = 0
    else:
        now = 1
    for y in range(a, a+8):
        for x in range(b, b+8):
            if x == b:
                now += 1
            if bwlst[now % 2] == arr[y][x]:
                now += 1
                continue
            now += 1
            cnt += 1

    if cnt > 32:
        cnt = 64 - cnt
    ans = min(ans, cnt)

n, m = map(int, input().split())
# n 세로길이 m 가로길이

arr = [list(input()) for _ in range(n)]

ans = float('inf')
for i in range(n-7):
    for j in range(m-7):
        dfs(i, j)

print(ans)