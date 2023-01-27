import sys
N = int(input())

arr = [int(sys.stdin.readline()) for i in range(N)]
arr.sort()

for i in range(N):
    print(arr[i])