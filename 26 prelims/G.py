def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    prefix = [0] * (3 * n + 1)

    for i in range(3 * n):
        prefix[i + 1] = prefix[i] + a[i]


    def range_sum(l, r):
        if l > r:
            return 0

        return prefix[r + 1] - prefix[l]

    def get_best(start, teams):
        if teams == 0:
            return 0

        end = start + 3 * teams - 1

        low = 0
        high = teams + 1

        while high - low > 1:

            k = (low + high) // 2

            x = start + 2 * (k - 1)
            y = x + 1
            z = end - k + 1

            yxz = a[x] + a[y] - 3 * a[z]

            if yxz >= 0:
                low = k
            else:
                high = k

        k = low

        ans = 4 * range_sum(start, start + 2 * k - 1)

        ans += 3 * range_sum(start + 2 * k, end - k)

        return ans

    ans = 0
    for i in range(n + 1):
        cur = 6 * range_sum(0, i - 1)

        cur += get_best(i, n - i)

        ans = max(ans, cur)

    print(ans)

t = int(input())

for _ in range(t):
    solve()