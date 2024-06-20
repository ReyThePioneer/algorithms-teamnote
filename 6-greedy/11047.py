#11047 동전 0

num_cointype, target = map(int, input().split())
cointype = []
cnt = 0

for _ in range(num_cointype):
    cointype.append(int(input()))

cointype.sort(reverse=True)

for coin in cointype:
    cnt += (target // coin)
    target %= coin

print(cnt)