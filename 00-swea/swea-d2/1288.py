T = int(input())

for i in range(T):
  n = int(input())
  s = set()
  k = 1

  while (True):
    for j in list(str(n)):
      s.add(j)
    
    if len(s) == 10:
      break

    n //= k
    k += 1
    n *= k
  
  print(f"#{i + 1} {n}")