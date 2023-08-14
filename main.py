arr = list(map(int, input().split()))
n = len(arr)
for i in range(n):
    cur = arr[i]
    pos = 0
    while pos < i and arr[pos] <= arr[i]:
        pos += 1
    for j in range(pos, i):
        arr[j], arr[i] = arr[i], arr[j]
print(arr)
