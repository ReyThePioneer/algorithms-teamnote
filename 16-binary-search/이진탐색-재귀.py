# 순차 탐색 : 리스트 안에 있는 특정한 '데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인'하는 방법
# 이진 탐색 : 정렬되어 있는 리스트에서 '탐색 범위를 절반씩 좁혀가며 데이터를 탐색'하는 방법 (탐색 범위 설정 : 시작점, 끝점, 중간점을 이용)

# 이진 탐색의 시간 복잡도 : O(log N) 보장
# 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 log2N에 비례함
# 예를 들어 초기 데이터가 32개일 때, 이상적으로 1단계를 거치면 16개 가량의 데이터만 남음 -> 2단계 8개 -> 3단계 4개

# 이진 탐색 소스코드 구현 (재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid

    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

# n(원소의 개수)과 target(찾고자 하는 값)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)