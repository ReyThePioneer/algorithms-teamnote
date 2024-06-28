#1961 숫자 배열 회전

T = int(input())

for t in range(T):
  N = int(input())
  arr = [list(map(int, input().split())) for _ in range(N)]
  arr_90 = list(map(list, zip(*arr[::-1])))
  arr_180 = list(map(list, zip(*arr_90[::-1])))
  arr_270 = list(map(list, zip(*arr_180[::-1])))

  print(f"#{t + 1}")
  for i in range(len(arr)):
    print(''.join(map(str, arr_90[i])), end=' ')
    print(''.join(map(str, arr_180[i])), end=' ')
    print(''.join(map(str, arr_270[i])), end='\n')