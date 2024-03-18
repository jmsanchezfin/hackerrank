N = int(input())

arr = []

for i in range(1, N + 1):
    arr.append(i)

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        print(arr[i], "x", arr[j])