#피보나치에 관한 문제는 아니지만, 재귀함수의 깊이에 관한 문제이기에 풀어보았다.

import sys
sys.setrecursionlimit(10**5)

def plus(n):
    if n == N:
       global sum
       sum = 0
    sum+=n
    if n == 0:
        return sum
    return plus(n-1)
N = int(input())
print(plus(N))

'''
문제를 풀며 재귀함수의 깊이 관한 부분보다 함수,전역,지역 변수에 관한 부분의 개념이 부족하다는 느낌이 들어 개념을 다시 한번 보완하였다.
'''
# 코드 보완
import sys
sys.setrecursionlimit(10**5)

def plus(n):
    global sum
    sum+=n
    if n == 0:
        return sum
    return plus(n-1)

sum = 0
print(plus(int(input())))




