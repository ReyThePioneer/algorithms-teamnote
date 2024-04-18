a, b = map(int, input().split())
dict = {a: 'A', b: 'B'}

# 1 차이 나면 큰 수가 이김
if abs(a - b) == 1:
  print(dict.get(max(a, b)))

# 2 차이 나면 작은 수가 이김
elif abs(a - b) == 2:
  print(dict.get(min(a, b)))