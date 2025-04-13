# Find the largest prime factor of 600851475143
def largest_prime_factor(n):
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return n

number = 600851475143
print("The largest prime factor is:", largest_prime_factor(number))