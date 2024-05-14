#2005 파스칼의 삼각형

T = int(input())

for tc in range(T):
  N = int(input())
  triangle = []

  for i in range(N):
    trirow = [1] * (i + 1)
    triangle.append(trirow)
  
    if (i > 1):
      for j in range(1, i):
        triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

  print(f"#{tc + 1}")

  for k in range(N):
    print(' '.join(map(str, triangle[k])))