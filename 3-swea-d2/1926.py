#1926 간단한 369게임

N = int(input())

for i in range(1, N + 1):
  ans_str = str(i)
  ans_str = ans_str.replace('3', '-')
  ans_str = ans_str.replace('6', '-')
  ans_str = ans_str.replace('9', '-')

if '-' in ans_str:
  for j in range(10):
    ans_str = ans_str.replace(f"{j}", '')
    print(ans_str, end= ' ')
  print()