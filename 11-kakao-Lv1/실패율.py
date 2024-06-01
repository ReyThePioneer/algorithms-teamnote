def solution(N, stages):
    answer = []
    remain = [0] * (N + 2)
    passed = [] * N
    difficulty = []
    
    for i in range(len(stages)):
        remain[stages[i]] += 1
    remain.remove(remain[0])
    
    for i in range(N + 1):        
        if i == 0:
            passed.append(len(stages))
        else:
            passed.append(passed[i-1] - remain[i-1])
    
    for i in range(N):
        difficulty.append(remain[i] / passed[i])
    
    sorted_difficulty = sorted(difficulty, reverse=True)
    rank = [sorted_difficulty.index(d) + 1 for d in difficulty]

    for _ in range(N):
        min_index = rank.index(min(rank))
        answer.append(min_index + 1)
        rank[min_index] = 501
        
    return answer