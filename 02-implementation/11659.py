#11659 구간 합 구하기 4

import sys

n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0] * (n + 1)

for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    sum = prefix_sum[j] - prefix_sum[i - 1]
    print(sum)