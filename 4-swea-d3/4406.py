#4406 모음이 보이지 않는 사람

T = int(input())

for tc in range(T):
  word = list(input())
  vowel = ['a', 'e', 'i', 'o', 'u']
  ans = ""

  for w in word:
    if w not in vowel:
      ans += w

  print(f"#{tc + 1} {ans}")