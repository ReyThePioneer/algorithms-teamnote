n = int(input())

for i in range(n):
  sum_odd = 0
  num_list = list(map(int, input().split()))

  for j in num_list:
    if j % 2 == 1:
      sum_odd += j

  print(f"#{i + 1} {sum_odd}")