#10814 나이순 정렬

# 회원 수 N 입력받기
n = int(input())

# N명의 회원 정보(나이, 이름) 입력받기
info = []
for _ in range(n):
    info.append(list(input().split()))

# 나이를 기준으로 오름차순 정렬하기
# 나이의 자료형을 int로
info.sort(key=lambda x:int(x[0]))

# [나이 이름] 출력하기
for i in info:
    print(f"{i[0]} {i[1]}")