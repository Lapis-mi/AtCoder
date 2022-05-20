def fibo(n):
    if n >= 2:
        return fibo(n-1) + fibo(n-2)
    else:
        return n

def fibonacci(n):
    print fibo(n)

fibonacci(1)
fibonacci(7)