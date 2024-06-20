# < 기본 입출력 >
# 프로그램 동작의 첫 번째 단계: 데이터를 입력받거나 생성하는 것

# input(): 한 줄의 문자열을 입력받는 함수
# map(): 리스트의 모든 원소에 각각 특정한 함수를 적용하는 함수

# 예) 공백을 기준으로 구분된 데이터를 입력받을 때 (리스트로)
# list(map(int, input().split()))
# 예) 공백을 기준으로 구분된 데이터의 개수가 많지 않다면
# a, b, c = map(int, input().split())


# < 입력을 위한 전형적인 소스코드 (1) >
# 데이터의 개수 입력받기
n = int(input())

# 각 데이터를 공백 기준 구분하기
data = list(map(int, input().split()))

# 내림차순 정렬
data.sort(reverse=True)
print(data)


# < 입력을 위한 전형적인 소스코드 (2) >
# n, m, k를 공백을 기준으로 구분하여 입력받기
n, m, k = map(int, input().split())
print(n, m, k)


# < 입력을 최대한 빠르게 받아야 하는 경우 (시간 초과 예방) >
# sys 라이브러리의 sys.stdin.readline() 이용
# 단, 입력 후 엔터가 줄 바꿈 기호로 입력되므로 rstrip() 함께 사용
import sys
data = sys.stdin.readline().rstrip()
print(data)


# < 자주 사용되는 표준 출력 방법 >
# print(): 기본 출력
# 각 변수를 콤마(,)로 띄어쓰기 구분하여 각각 출력 가능
# 출력 이후 줄 바꿈 수행, 줄 바꿈 원치 않는 경우 'end' 속성 이용

# 출력할 변수들
a = 1
b = 2
print(a, b)
print(7, end=" ")
print(8, end=" ")

answer = 7
print("정답은 " + str(answer) + "입니다.")


# < f-string 예제 >
# 문자열과 수 데이터를 간단하게 함께 출력할 때 사용
# 문자열 앞에 접두사 'f'를 붙여 사용
answer = 7
print(f"정답은 {answer}입니다.")