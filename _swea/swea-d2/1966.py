T = int(input())

for t in range(T):
  N = int(input())
  input_list = sorted(list(map(int, input().split())))
  input_list = ' '.join(map(str, input_list))
  print(f"#{t + 1} {input_list}")