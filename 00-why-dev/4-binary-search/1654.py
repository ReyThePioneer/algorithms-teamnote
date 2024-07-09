#1654 랜선 자르기

import sys

# 이미 가지고 있는 랜선의 개수 K, 필요한 랜선의 개수 N 입력받기
k, n = map(int, sys.stdin.readline().split())

# K개의 랜선 길이 입력받기
lan = []
for _ in range(k):
    lan.append(int(sys.stdin.readline()))

# 랜선 길이 정렬
lan.sort()

# 이분 탐색 범위 : 최소~최대 길이
start = 1
end = max(lan)

# start와 end가 같아질 때까지 탐색
while start <= end:
    mid = (start + end) // 2
    lines = 0

    # 모든 랜선을 mid로 나눠서 몇 개가 나오는지 본다
    for i in lan:
        lines += (i // mid)

    # 잘랐을 때 필요한 개수 이상이면
    if lines >= n:
        start = mid + 1
    # 잘랐을 때 필요한 개수 이하면
    else:
        end = mid - 1
        
# 최대 랜선의 길이 출력
print(end)