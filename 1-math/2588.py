#2588 곱셈

one = int(input())
two = list(map(int, input()))

three = one * two[2]
four = one * two[1]
five = one * two[0]
six = three + (four * 10) + (five * 100)

print(three, four, five, six, sep='\n')