import sys
input = sys.stdin.readline

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

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
v = [0] * (max(lst) + 1)

for i in lst:
    if not v[i]:
        v[i] = 1
        dfs([i])
        v[i] = 0