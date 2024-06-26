#1181 단어 정렬

import sys

# 단어 개수 N 입력받기
n = int(sys.stdin.readline())
words = []
words_len = []

# N개의 단어 입력받기
for _ in range(n):
    words.append(sys.stdin.readline().replace('\n', ''))

# 중복 단어 제거
words = set(words)
words = list(words)

# 각 단어 길이 구하기
for word in words:
    words_len.append([word, len(word)])

# 길이가 같은 경우 알파벳 순서대로 정렬하기
words_len.sort(key=lambda x:x[0])

# 길이가 짧은 순서대로 정렬하기
words_len.sort(key=lambda x:x[1])

# 정렬된 단어들을 한 줄에 하나씩 출력하기
for w in words_len:
    print(w[0])