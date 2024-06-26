#1181 단어 정렬

import sys

# 단어 개수 N 입력받기
n = int(sys.stdin.readline())

# set에 N개의 단어 입력받기
words = set()
for _ in range(n):
    words.add(sys.stdin.readline().strip())

# 2차원 list에 [길이, 단어] 입력하기
len_word = []
for word in words:
    len_word.append([len(word), word])

# 길이가 짧은 순서대로 정렬하기 (길이가 같은 경우 알파벳 순서대로 정렬)
len_word.sort()

# 정렬된 단어들을 한 줄에 하나씩 출력하기
for w in len_word:
    print(w[1])