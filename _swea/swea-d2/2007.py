T = int(input())

for t in range(T):
  input_str = input()
  pattern = 0

  for i in range(1, len(list(input_str))):
    pattern = input_str[:i]

    if input_str[i:(i + len(list(pattern)))] == pattern:
      print(f"#{t + 1} {len(pattern)}")
      break