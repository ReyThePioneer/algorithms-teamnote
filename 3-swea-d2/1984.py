#1984 중간 평균값 구하기

T = int(input())

for tc in range(T):
  arr = list(map(int, input().split()))
  ans = 0

  arr.sort()
  arr.pop(0)
  arr.pop(-1)
  ans = sum(arr) / len(arr)

  print(f"#{tc + 1} {round(ans)}")