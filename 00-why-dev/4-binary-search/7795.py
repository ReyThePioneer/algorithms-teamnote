#7795 먹을 것인가 먹힐 것인가

import sys
import bisect

# 테스트 케이스의 개수 T 입력받기
T = int(sys.stdin.readline())

# 각 테스트 케이스마다 N, M, A, B 입력받기
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    # B 배열 정렬
    B.sort()

    # B 배열에서 A[i]보다 큰 값의 개수 찾기
    cnt = 0
    for a in A:
        # B에서 a보다 '작은' 원소가 '시작'되는 인덱스
        idx = bisect.bisect_left(B, a)
        cnt += idx

    # 각 테스트 케이스마다 A의 원소가 B보다 큰 쌍의 개수 출력
    print(cnt)