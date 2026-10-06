
def solve():
    n, k = map(int, input().split())
    s = input().strip()

    a = []

    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        if s[i] == 'G' and cnt1 < k + 1:
            cnt1 += 1
        else:
            a.append(s[i])

    firstG = False
    m = len(a)
    for i in range(m):
        if firstG == True:
            if a[i] == 'G':
                cnt2 += 1
            else:
                cnt2 += 2
        else:
            if a[i] == 'G':
                firstG = True

    # print(cnt1, cnt2)

    if cnt2 > k:
        print("NO")
    else:
        print("YES")



t = int(input())
for _ in range(t):
    solve()