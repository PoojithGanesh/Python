ef count(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    a,b=1,1
    for _ in range(2,n+1):
        a,b=b,a+b
    return b
n=int(input("enter the no of steps:"))
print("No.of distinct ways to climb:", count(n))