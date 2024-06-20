import statistics

n = int(input())

for i in range(n):
  test_case = list(map(int, input().split()))
  average = statistics.mean(test_case)
  print(f"#{i + 1} {average:.0f}")