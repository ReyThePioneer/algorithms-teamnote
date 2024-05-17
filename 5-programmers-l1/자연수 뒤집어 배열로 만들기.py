def solution(n):
    answer = []
    
    for i in str(n):
        answer.append(i)
    answer.reverse()
    answer = list(map(int, answer))
    
    return answer