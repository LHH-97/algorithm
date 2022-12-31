#코드 1
def solution(sizes):
    for i in sizes:
        if i[0] <= i[1]:
            a = i[0]
            i[0] = i[1]
            i[1] = a
    cnt = sizes[0][1]
    for j in sizes:
        if j[1] > cnt:
            cnt = j[1]
    max_w = max(sizes)[0]
    sum = cnt*max_w
    return sum
    
#코드 2
def solution(sizes):
    return max(max(i) for i in sizes) * max(min(i) for i in sizes)