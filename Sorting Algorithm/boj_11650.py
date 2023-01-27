import sys

N = int(input())
arr = []

for i in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))
arr.sort(key = lambda x:(x[0],x[1]))

for i in arr:
    print(i[0],i[1])

#sort()함수는 이차원리스트를 [0]기준으로 정렬한 후 그것을 기반으로 [1]을 기준으로 정렬을 실시한다.
# sort()함수의 key에 lambda 표현식을 이용해 정렬의 기준을 정의할 수 있다.  