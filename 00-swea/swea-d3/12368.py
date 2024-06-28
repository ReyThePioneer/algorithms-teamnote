#12368 24시간

T = int(input())

for tc in range(T):
  A, B = map(int, input().split())
  
  time = (A + B) % 24

  print(f"#{tc + 1} {time}")