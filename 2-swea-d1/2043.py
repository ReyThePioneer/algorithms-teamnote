p, k = map(int, input().split())
cnt = 0

while (p != k):
  cnt += 1
  k += 1

print(cnt + 1)