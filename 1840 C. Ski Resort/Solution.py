t = int(input())
for _ in range(t):
    n, k, q = map(int, input().split())
    wea_for = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for idx, a in enumerate(wea_for):
        if a <= q:
            cnt += 1
        else:
            if cnt >= k:
                ans += (cnt - k + 1) * (cnt - k + 2) // 2
            cnt = 0
    if cnt >= k:
            ans += (cnt - k + 1) * (cnt - k + 2) // 2
    print(ans)
