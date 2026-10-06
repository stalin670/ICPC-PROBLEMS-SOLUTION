
def solve():
    n, c = map(int, input().split())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))

    for i in range(n):
        p[i] -= 1

    vis = [False] * n
    ans = 0

    for i in range(n):
        if vis[i] == False:
            len , idx = 0, i
            totalProfit = 0
            single = 0
            while vis[idx] == False:
                vis[idx] = True
                len += 1

                single += max(0, a[idx] - c)
                totalProfit += a[idx]

                idx = p[idx]

            totalProfit -= (len - 1) * c 
            ans += max({0, single, totalProfit})

    print(ans)

t = int(input())
for _ in range(t):
    solve()