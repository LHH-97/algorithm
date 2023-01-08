
i = 1
while(True):

    L,P,V = map(int,input().split())
    if L == 0 and P == 0 and V == 0:
        break
    cnt = V//P
    res = V%P
    result = cnt*L

    if res > L:
        result+=L
    else:
        result += res
    print('Case ',i,': ', result,sep = '')
    i+=1