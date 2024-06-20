# 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제
# 따라서 단순히 시각을 1씩 증가시키면서 3이 하나라도 포함되어 있는지 확인
# 완전 탐색(Brute Forcing) : 가능한 경우의 수를 모두 검사해보는 탐색 방법

h = int(input())
cnt = 0

for i in range(h + 1):
  for j in range(60):
    for k in range(60):
      # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
      if '3' in str(i) + str(j) + str(k):
        cnt += 1

print(cnt)