#2947 나무 조각

# 초기 나무조각 순서 입력받기
import sys
arr = list(map(int, sys.stdin.readline().split()))

# 버블 정렬
# 배열의 개수(5)만큼 반복, 전체 배열 순회 (0~4)
for i in range(len(arr)):
    # 정렬된 부분 제외 순회 (0~3, 0~2, 0~1, 0)
    for j in range(len(arr) - i - 1):

        # 앞의 원소가 뒤의 원소보다 큰 경우 swqp
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

            # swap 될 때마다 나무조각 순서 출력
            print(" ".join(map(str, arr)))
