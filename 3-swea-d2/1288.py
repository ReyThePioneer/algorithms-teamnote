T = int(input())
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(T):
  N = int(input())
  k = 1
  num_list = []

  while (True):
    k += 1
    str_N = list(str(N * k))
    num_list.extend(str_N)
    
    a = list(map(int, list(set(num_list))))
    a.sort()

    if a == num:
      print(f"#{T + 1} {N * k}")
      break