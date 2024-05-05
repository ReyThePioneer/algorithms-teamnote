t = int(input())

for i in range(t):
  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  array = []

  if (n > m):
    m, n = n, m
    a, b = b, a

  while (n <= len(b)):
    sum = 0
    for j in range(n):
      sum += a[j] * b[j]
    array.append(sum)
    b.remove(b[0])

  print(f"#{i + 1} {max(array)}")