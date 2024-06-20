#1289 원재의 메모리 복구하기

T = int(input())

for tc in range(T):
  mem = list(str(int(input())))

  check = '1'
  cnt = 0

  for i in mem:
    if i == check:
      cnt += 1
      
      if check == '1':
        check = '0'
      else:
        check = '1'

  print(f"#{tc + 1} {cnt}")