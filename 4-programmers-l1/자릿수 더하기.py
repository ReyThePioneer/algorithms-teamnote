def solution(num):
    sum = 0

    a = list(str(num))

    for i in range(len(a)):
        sum += int(a[i])

solution(123)