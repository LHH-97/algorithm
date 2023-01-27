#7568번-덩치
N = int(input())
arr = []
for i in range(N):
    a,b = map(int,input().split())
    arr.append((a,b))

for j in range(N):
    k = 1
    for p in range(N):
        #if arr[j] == arr[p]:
        #  continue    #arr[0]과 arr[0]을 비교할시 의미가 없으니 continue를 하였으나, 없어도 되는 코드로 판단된다.   
        if arr[j][0] < arr[p][0] and arr[j][1] < arr[p][1]:
            k+=1
    print(k,end = ' ')


'''
a = tuple(1,2) 
TypeError: tuple expected at most 1 argument, got 2

위의 에러 코드에 대한 설명대로 tuple()에는 1 argument가 와야 한다. list()도, int()도 마찬가지 이다. 

AttributeError: 'tuple' object has no attribute 'append'

tuple은 append 함수를 지원하지 않는다. 

'''