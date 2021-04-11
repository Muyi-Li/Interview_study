def factorial(nums):
    if nums in [0,1]:
        return 1
    else:
        return nums * factorial(nums-1)

#print(factorial(3))

def fibonacci(n):
    assert n >= 0 and int(n) == n, 'Fibonacci number cannot be negative number of non-integer'
    if n ==0:
        return n
    elif n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
#print(fibonacci(7))

def sum_digits(n):
    assert n >= 0 and int(n) == n, 'n has to be positive'
    if n == 0:
        return 0
    else:
        return int(n%10) + sum_digits(n//10)
print(sum_digits(10))