#1979 어디에 단어가 들어갈 수 있을까

T = int(input())

def count(arr) :
  total = 0

  for lst in arr :
    cnt = 0

    for i in range(len(lst)) :
      if lst[i] == 1 :
        cnt += 1

      else:
        if cnt == K :
          total += 1

        cnt = 0

  return total

for t in range(T) :
  N, K = map(int, input().split())

  arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 1)]

  arr_t = list(map(list, zip(*arr)))
  ans = count(arr) + count(arr_t)

  print(f"#{t + 1} {ans}")