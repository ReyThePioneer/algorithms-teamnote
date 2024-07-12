#1010 다리 놓기

import sys
import math

# 테스트 케이스의 수 T 입력받기
T = int(sys.stdin.readline())

# 각 테스트 케이스마다 N, M 입력받기
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    # 다리를 놓을 수 있는 경우의 수 계산하기 (mCn)
    bridges = math.factorial(M) // (math.factorial(N) * math.factorial(M - N))

    print(bridges)