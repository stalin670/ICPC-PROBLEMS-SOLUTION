def solve():
    n = int(input())
    a = list(map(int, input().split()))

    b = []
    for i in range(n):
        nxt = i + 1
        if nxt == n:
            nxt = 0
        diff = abs(a[i] - a[nxt])
        b.append(diff)

    b.sort()
    print(b[n - 2])

t = int(input())

for _ in range(t):
    solve()