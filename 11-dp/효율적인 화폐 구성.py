# <문제> 효율적인 화폐 구성
# M원을 만들기 위한 최소한의 화폐 개수 (화폐 종류는 N가지)

n, m = map(int, input().split())

# n종류의 화폐 단위 입력받기
array = []
for _ in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장할 dp table 초기화
d = [10001] * (m + 1)

# DP 진행 (Bottom-up)
d[0] = 0
for i in range(n): # i는 각각의 화폐 단위
    for j in range(array[i], m + 1): # j는 각각의 금액
        # (i - k)원을 만드는 방법이 존재하는 경우
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
# 최종적으로 M원을 만드는 방법이 없는 경우
if d[m] == 10001:
    print(-1)
else:
    print(d[m])