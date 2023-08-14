arr = list(map(int, input().split()))
n = len(arr)
ans = []
ans_len = 0
for i in range(n):
    cur = arr[i]
    pos = ans_len
    for j in range(len(ans)):
        if cur <= ans[j]:
            pos = j
            break
    ans.insert(pos, cur)
    ans_len += 1
print(ans)
