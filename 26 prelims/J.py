def solve():
    s00, s01, s10, s11 = map(int, input().split())

    ans = ""
    def checker(s):
        nonlocal ans
        if len(ans) == 0 or s < ans:
            ans = s


    def helper(s00, s01, s10, s11):
        cur = ""
        while s00 > 0 and s11 > 0:
            cur += "00"
            s00 -= 1
            s11 -= 1

        while s00 > 0 and s01 > 0:
            cur += "00"
            s00 -= 1
            s01 -= 1

        while s00 > 0:
            cur += "0"
            s00 -= 1

        while s10 > 0:
            cur += "0"
            s10 -= 1

        while s11 > 0 and s01 > 0:
            cur += "01"
            s11 -= 1
            s01 -= 1

        while s01 > 1:
            cur += "01"
            s01 -= 2

        while s01 > 0:
            cur += "1"
            s01 -= 1

        while s11 > 0:
            cur += "1"
            s11 -= 1

        return cur

    if s00 > 0:
        s = helper(s00 - 1, s01, s10, s11) + "00"
        checker(s)

    if s01 > 0:
        s = helper(s00, s01 - 1, s10, s11) + "01"
        checker(s)

    if s10 > 0:
        s = helper(s00, s01, s10 - 1, s11) + "10"
        checker(s)

    if s11 > 0:
        s = helper(s00, s01, s10, s11 - 1) + "11"
        checker(s)

    print(ans)

t = int(input())

for _ in range(t):
    solve()