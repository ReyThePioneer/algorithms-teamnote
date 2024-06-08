# 나의 풀이
def solution(n, arr1, arr2):
    map = [['0' for _ in range(n)] for _ in range(n)]
    answer = [''] * n

    for i in range(n):
        # 10진수를 2진수로
        arr1[i] = bin(arr1[i])[2:]
        arr2[i] = bin(arr2[i])[2:]
        # 앞에 '0' 추가
        if len(arr1[i]) < n:
            arr1[i] = '0' * (n - len(arr1[i])) + arr1[i]
        if len(arr2[i]) < n:
            arr2[i] = '0' * (n - len(arr2[i])) + arr2[i]
    
    
    for i in range(n):
        for j in range(n):
            # 두 지도 합치기
            if arr1[i][j]=='1' or arr2[i][j]=='1':
                map[i][j] = '1'
            if arr1[i][j]=='0' and arr2[i][j]=='0':
                map[i][j] = '0'
            # 1을 #으로, 0을 공백으로
            if map[i][j]=='1':
                map[i][j] = '#'
            else:
                map[i][j] = ' '
            # map을 1차원 배열로 정리
            answer[i] += map[i][j]
        
    return answer

# 다른 사람의 풀이
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer