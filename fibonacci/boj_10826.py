#재귀호출 깊이 제한을 늘림. 
import sys
sys.setrecursionlimit(10**5)

dic = {0:0,1:1}
def fib(n):
    if n in dic:
        return dic[n]
    dic[n] = fib(n-1)+fib(n-2)
    return dic[n]
print(fib(int(input())))

#재귀함수를 사용하지 않고, 반복문을 사용한 코드
arr = [0,1,1]
n = int(input())
for i in range(3,n+1):
    arr.append(arr[i-1]+arr[i-2])
print(arr[n])
