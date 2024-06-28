n = int(input())
num_called = list(map(int, input().split()))

num_cnt = [0] * 23

for i in num_called:
  num_cnt[i - 1] += 1

print(' '.join(map(str, num_cnt)))