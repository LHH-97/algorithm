#Pass Code
dic = {0:0,1:1}
def fibo(n):
    if n in dic:
        return dic[n]
    dic[n] = fibo(n-1)+fibo(n-2)
    return dic[n]

print(fibo(int(input())))

#시간 초과(중복호출의 문제가 존재하고 약 2**n번 만큼 호출을 하게되어 시간초과가 된다. )
def fibo(n):
    if n ==1 or n == 2:
        return 1
    return fibo(n-1)+fibo(n-2)

print(fibo(int(input())))