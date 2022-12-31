def solution(answers):
    value = []
    cnt= len(answers) //5
    arr = []
    one = [1,2,3,4,5]*(cnt+1)
    two = [2,1,2,3,2,4,2,5]*(cnt+1)
    three = [3,3,1,1,2,2,4,4,5,5]*(cnt*2+2)
    arr = [one,two,three]
    cnt = 0
    for j in range(3):
        for i in range(len(answers)):
            if arr[j][i] == answers[i]:
                cnt+=1
        arr[j] = cnt
        cnt = 0
        
    max_arr = max(arr)
    for i in range(3):
        if max_arr == arr[i]:
            value.append(i+1)
    return value