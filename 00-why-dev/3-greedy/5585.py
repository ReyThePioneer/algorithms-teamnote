#5585 거스름돈

import sys

# 물건의 가격 입력받기
price = int(sys.stdin.readline())

# 거슬러줘야 하는 금액 계산
change = 1000 - price

# 가장 큰 화폐 단위부터 돈을 거슬러주며 잔돈의 개수 세기
change_cnt = 0

coin_types = [500, 100, 50, 10, 5, 1]

for coin in coin_types:
    change_cnt += change // coin
    change %= coin

# 잔돈의 개수 출력하기
print(change_cnt)