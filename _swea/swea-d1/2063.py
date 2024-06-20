import statistics

n = int(input())
scores = list(map(int, input().split()))

print(statistics.median(scores))