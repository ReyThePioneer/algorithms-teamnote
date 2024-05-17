#1204 최빈수 구하기

T = int(input())

for tc in range(T):
  score_arr = list(map(int, input().split()))
  score_arr.sort()
  ans = 0

  print(f"#{tc + 1} {ans}")