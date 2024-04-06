a, m, d, n = map(int, input().split())
array = [0] * n

array[0] = a
for i in range(1, n):
  array[i] = array[i - 1] * m + d

print(array[n - 1])