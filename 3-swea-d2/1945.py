n = int(input())

for i in range(n):
  N = int(input())
  pwr = [2, 3, 5, 7, 11]
  ans = [0, 0, 0, 0, 0]
  
  for j in range(5):
    while (N % pwr[j] == 0):
      ans[j] += 1
      N = N / pwr[j]
  
  print(f"#{i + 1} {' '.join(map(str, ans))}")