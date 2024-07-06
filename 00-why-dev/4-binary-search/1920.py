#1920 수 찾기

import sys

# N 입력받기
N = int(sys.stdin.readline())

# N 크기의 A 리스트 입력받고 set으로 바꾸기
A = set(map(int, sys.stdin.readline().split()))

# M 입력받기
M = int(sys.stdin.readline())

# M 크기의 B 리스트 입력받기
B = list(map(int, sys.stdin.readline().split()))

# B에 있는 수들이 각각 A에 존재하는지 확인
for b in B:
    if b in A:
        print(1)
    else:
        print(0)