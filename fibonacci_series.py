def fibonacci(n):
    if n < 0:
        print("Invalid Input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 10
print("Fibonacci Sequence : ")
for i in range(n):
    print(fibonacci(i))
