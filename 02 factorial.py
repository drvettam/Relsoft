def factorial(n):
    r=1
    while n>0:
        r=r*n
        n=n-1
    return r
n=5
print("Factorial of ",n,"is ",factorial(n))
