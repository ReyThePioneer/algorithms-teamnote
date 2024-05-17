#1859 백만 장자 프로젝트

T = int(input())

for tc in range(T):
  day = int(input())
  price = list(map(int, input().split()))
  benefit = 0
  max = price[day - 1]
  
  for i in range(day - 1, -1, -1):
    if price[i] >= max:
      max = price[i]
    benefit += max - price[i]

  print(f"#{tc + 1} {benefit}")