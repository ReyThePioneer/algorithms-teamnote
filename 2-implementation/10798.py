#10798 세로읽기

import sys

# 문자열 다섯 줄 입력받기
arr = []
for _ in range(5):
    arr.append(sys.stdin.readline().strip())

# 가장 긴 문자열의 길이
max_len = len(max(arr, key=len))

# 세로로 출력하기
for i in range(max_len):
    for a in arr:
        if i < len(a): # 현재 문자열이 i번째 문자를 가지고 있으면
            print(a[i], end="")