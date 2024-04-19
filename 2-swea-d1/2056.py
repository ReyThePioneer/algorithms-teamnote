n = int(input())


for i in range(n):
  yyyymmdd = input()
  y = int(yyyymmdd[0:4])
  m = int(yyyymmdd[4:6])
  d = int(yyyymmdd[6:8])

  def print_date():
    print(" ", yyyymmdd[0:4], "/", yyyymmdd[4:6], "/", yyyymmdd[6:8], sep='')

  print(f"#{i + 1}", end='')
  if (1 <= m <= 12):
    if (m in {1, 3, 5, 7, 8, 10, 12}) and (1 <= d <= 31):
      print_date()
    elif (m in {4, 6, 9, 11}) and (1 <= d <= 30):
      print_date()
    elif (m == 2) and (1 <= d <= 28):
      print_date()
    else:
      print(f" -1")
  else:
    print(f" -1")