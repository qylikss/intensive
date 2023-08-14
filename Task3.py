arr = list(map(int, input().split()))
n = len(arr)
ans = []
for i in range(n):
    cur = arr[i]
    pos = 0
    ans.append(cur)
    for j in range(len(ans)):
        if cur >= ans[j]:
            pos = j
    ans[pos] = cur
print(ans)