n = int(input())
num_called = list(map(int, input().split()))
num_called.reverse()

print(' '.join(map(str, num_called)))