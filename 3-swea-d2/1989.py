T = int(input())

for i in range(T):
  test_case = input()
  ans = 0

  for j in range(len(test_case) // 2):
    if test_case[j] == test_case[-1 - j]:
      ans = 1

  print(f"#{i + 1} {ans}")