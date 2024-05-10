#1979 어디에 단어가 들어갈 수 있을까

T = int(input())

for t in range(T):
  N, K = map(int, input().split())
  arr = []

  for i in range(N):
    arr[i] = list(map(int, input().split()))
    sum_arr = []
    sum = 0
    print(arr)

    for j in range(N):
      while (arr[i][j] == 1):
        sum += 1
    sum_arr.append(sum)

  # print(f"#{t + 1} {ans}")