money = [500,100,50,10,5,1]
pay = 1000 - int(input())
cnt = 0
for i in money:
    cnt += pay//i
    pay%=i
print(cnt)
