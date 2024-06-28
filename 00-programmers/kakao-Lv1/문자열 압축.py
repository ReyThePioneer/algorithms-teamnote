# Lv.2 문자열 압축

def solution(s):
    len_input = len(s)
    len_comp = [len_input] # 초기값 : 압축 전 길이

    for unit in range(1, len_input):
        str_comp = ""
        # string 개수 단위로 쪼개기
        str_split = [s[i:i+unit] for i in range(0, len_input, unit)]
        cnt = 1
    
        for j in range(1, len(str_split)):
            prev, cur = str_split[j-1], str_split[j]
            # 이전 문자와 같으면
            if prev == cur:
                cnt += 1
            # 이전 문자와 다르면
            else:
                str_comp += (str(cnt) + prev) if cnt > 1 else prev
                cnt = 1 # 초기화
        
        str_comp += (str(cnt) + str_split[-1]) if cnt > 1 else str_split[-1]
        len_comp.append(len(str_comp))

    return min(len_comp)