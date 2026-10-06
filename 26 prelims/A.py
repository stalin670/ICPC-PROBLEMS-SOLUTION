def solve():
    x, a, b = map(int, input().split())

    if x < 80:
        ans = (80 - x) * a + 20 * b
    else:
        ans = (100 - x) * b

    print(ans)


t = int(input())

for _ in range(t):
    solve()