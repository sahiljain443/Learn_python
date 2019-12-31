# print fibonnaci number till nth number

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fib(n-1) + fib(n-2))
    
x = input ("Till what no. you want fibonnaci: ")

for y in range (int(x)):
    print(fib(y))