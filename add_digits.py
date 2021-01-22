def sum_digits(n):
    _sum = 0
    if n <= 9:
        return n
    else:
        last = n%10
        other = n//10
        return sum_digits(other) + last