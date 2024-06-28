n = int(input())
sum = 0
last = 1

while (n > sum):
  sum += last
  last += 1

print(last - 1)