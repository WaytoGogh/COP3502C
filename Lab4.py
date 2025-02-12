def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a+b
    return b

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(6))
print(fibonacci(25))

#prime numbers

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(is_prime(2))
print(is_prime(11))
print(is_prime(1741))
print(is_prime(1))
print(is_prime(9))
print(is_prime(-2))

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

print_prime_factors(10)
print_prime_factors(2)
print_prime_factors(24)
print_prime_factors(2475)
print_prime_factors(23)