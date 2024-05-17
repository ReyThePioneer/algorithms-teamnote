#1204 최빈수 구하기

T = int(input())

for tc in range(T):
  _ = int(input())
  scores = list(map(int, input().split()))
  freq = [0] * 101
  mode = 0

  for score in scores:
    freq[score] += 1
    if freq[score] >= freq[mode]:
      mode = score
  
  print(f"#{tc + 1} {mode}")