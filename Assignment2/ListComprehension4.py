#How can you use list comprehension to generate a list of the first 10 Fibonacci numbers?
def fibonacci(n):
    fib = [0, 1]
    [fib.append(fib[-1] + fib[-2]) for i in range(n - 2)]
    return fib

print(fibonacci(10))
