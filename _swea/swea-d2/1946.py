#1946 간단한 압축 풀기

T = int(input())

for tc in range(T):
  N = int(input())
  str_arr = []

  for _ in range(N):
    C, K = map(str, input().split())

    for _ in range(int(K)):
      str_arr.append(C)
  
  print(f"#{tc + 1}")
  for i in range(0, len(str_arr), 10):
    print(''.join(map(str, str_arr[i : i + 10])))