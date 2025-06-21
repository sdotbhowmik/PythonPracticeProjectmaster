def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0
    sub = 0
    for i in range(n):
        time_available = a[i] - sub
        if time_available >= b[i]:
            count += 1
            sub = a[i]
    print(count)

t = int(input())
for i in range(t):
    solve()