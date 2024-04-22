def solution(n):
    answer = ''
    l = []
    
    for i in str(n):
        l.append(i)
    l.sort(reverse=True)
    
    for i in l:
        answer += i
    answer = int(answer)
    
    return answer