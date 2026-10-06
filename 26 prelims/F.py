
def solve():
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        x, y = map(int, input().split())
        a.append((x, y))
        b.append((y, x))

    a.sort()
    b.sort()

    cnt1 = 0
    cnt2 = 0
    for i in range(1, n):
        if a[i][1] < a[i - 1][1]:
            cnt1 += 1
        if b[i][1] < b[i - 1][1]:
            cnt2 += 1

    if cnt1 <= 1 or cnt2 <= 1:
        print("YES")
    else:
        print("NO")


t = int(input())
for _ in range(t):
    solve()