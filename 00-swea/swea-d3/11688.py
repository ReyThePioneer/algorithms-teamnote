#11688 Calkin-Wilf tree 1

T = int(input())

for tc in range(T):
  directions = input()
  a = 1
  b = 1
  
  for direction in directions:
    if direction == 'L':
      b = a + b
    elif direction == 'R':
      a = a + b

  print(f"#{tc + 1} {a} {b}")