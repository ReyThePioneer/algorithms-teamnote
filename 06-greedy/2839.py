#2839 설탕 배달

sugar = int(input())
bag = 0

while (sugar >= 0):
  # 5로 나누어 떨어지는 경우
  if sugar % 5 == 0:
    bag += (sugar // 5)
    break
  
  # 5와 3의 조합으로 나누어 떨어지는 경우
  # 5의 배수가 될 때까지 설탕 -3kg, 봉지 +1
  sugar -= 3
  bag += 1

# 그래도 나누어 떨어지지 않는 경우
else:
  bag = -1

print(bag)