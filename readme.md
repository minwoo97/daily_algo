# 10월 21일

### 체스판 다시 칠하기
로직으로는 일단 w, b를 체크해야하는데 8 * 8 배열이니까 바뀌는 횟수는 32회가 넘는다면 그 반대로 바꾸는게 더 효율적! 
그래서일단 지금 주어진 상태로 체스판을 완성시키는데 필요한 횟수를 세고, 
순회하면서 y축이 바뀔때는 그 색이 그대로 다시 j == 0일때 들어가야함
그런 로직을 적용한 것

```
def dfs(a, b):
    global ans
    # 개수로 세려햇는데 걍 순회하면서 해야겟다
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

n, m = map(int, input().split()) # n 세로길이 m 가로길이

arr = [list(input()) for _ in range(n)]

ans = float('inf')
for i in range(n-7):
    for j in range(m-7):
        if i == 0 and j == 5:
            asdf = 1
        dfs(i, j)


print(ans)
```

