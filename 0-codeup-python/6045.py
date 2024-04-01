a, b, c = list(map(int, input().split(' ')))
sum = a + b + c
avg = format(sum / 3, ".2f")

print(sum, avg)