#1926 간단한 369게임

N = int(input())

for i in range(1, N + 1):
  ans_str = str(i)
  clap = ''

  for j in ans_str:
    if int(j) == 0:
      continue
    elif int(j) % 3 == 0:
      clap += '-'

  if len(clap) == 0:
    print(i, end=' ')
  else:
    print(clap, end=' ')