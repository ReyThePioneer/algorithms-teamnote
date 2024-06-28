#11399 ATM

people = int(input())
time = list(map(int, input().split()))
total_time = []

time.sort()

for i in range(1, people + 1):
    total_time.append(sum(time[0:i]))

print(sum(total_time))