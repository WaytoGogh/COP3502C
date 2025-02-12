def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a+b
    return b

#prime numbers

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


#Prime Factorization
def print_prime_factors(n):
    original_n = n  
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(str(divisor))
            n //= divisor
        divisor += 1

    print(original_n, "=", " * ".join(factors))

