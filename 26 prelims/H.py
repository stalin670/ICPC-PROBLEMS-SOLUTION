def get_modular_inverses(n, mod=998244353):
    inv = [0] * (n + 1)
    
    if n >= 1:
        inv[1] = 1
        
    for i in range(2, n + 1):
        inv[i] = (mod - mod // i) * inv[mod % i] % mod
        
    return inv

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    mod = 998244353

    inv = get_modular_inverses(n)
    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + inv[i]
        pref[i] %= mod

    ans = 0
    for i in range(n):
        leftIdx, rightIdx = i, n - i - 1
        leftexpected = pref[leftIdx] % mod
        rightexpected = pref[rightIdx] % mod
        ans = ans + (leftexpected + rightexpected) * a[i]
        ans %= mod

    print(ans)


t = int(input())

for _ in range(t):
    solve()