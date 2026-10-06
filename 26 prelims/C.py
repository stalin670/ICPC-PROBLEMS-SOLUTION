def solve():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))

    x.sort()

    l = x[0] - 1
    r = n - x[m - 1]

    maxDiff = 0
    for i in range(m - 1):
        maxDiff = max(maxDiff, abs(x[i + 1] - x[i] - 1))

    if l + r >= maxDiff:
        print(min(2*l + r, l + 2*r))
    else:
        maxDiff = maxDiff - l - r
        l += maxDiff
        ans = min(2*l + r, l + 2*r)
        l -= maxDiff
        r += maxDiff
        ans = min(ans, min(2*l + r, l + 2*r))
        print(ans)



t = int(input())

for _ in range(t):
    solve()