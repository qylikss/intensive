arr = list(map(int, input().split()))
n = len(arr)
ans = [None] * n
ans[0] = arr[0]
for i in range(1, n):
    cur = arr[i]
    pos = i - 1
    while pos >= 0 and ans[pos] > cur:
        ans[pos + 1] = ans[pos]
        pos -= 1
    ans[pos + 1] = cur
print(ans)