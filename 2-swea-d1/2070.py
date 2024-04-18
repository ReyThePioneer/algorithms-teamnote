n = int(input())

for i in range(n):
  a, b = map(int, input().split())
  if (a < b):
    operator = "<"
  elif (a == b):
    operator = "="
  else:
    operator = ">"
  print(f"#{i + 1} {operator}")