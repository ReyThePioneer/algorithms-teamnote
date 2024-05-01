T = int(input())

for i in range(T):
  N, M = map(int, input().split())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  array = []
  sum = 0

  if (N < M):
    for j in range(M - N + 1):
      cnt = 0
      for k in range(i, i + N):
        sum += A[cnt] * B[k]
        cnt += 1
      array.append(sum)
      sum = 0
  
  elif (N > M):
    for l in range(N - M + 1):
      cnt = 0
      for m in range(l, l + M):
        sum += A[m] * B[cnt]
        cnt += 1
      array.append(sum)
      sum = 0
  
  else:
    for n in range(N):
      sum += A[n] * B[n]
    array.append(sum)

  print(f"#{i + 1} {max(array)}")