T = int(input())

for t in range(T):
  N = int(input())
  C = []

  for n in range(N):
    C.append(list(map(int, input().split())))
    dis = 0
    vel = 0

    for i in range(len(C)):
      if C[i][0] == 0:
        dis += vel

      elif C[i][0] == 1:
        vel += C[i][1]
        dis += vel

      elif C[i][0] == 2:
        if vel < C[i][1]:
          vel = 0
          continue
        vel -= C[i][1]
        dis += vel

  print(f"#{t + 1} {dis}")