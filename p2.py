# Sum of even Fibonacci numbers not exceeding 4 million
a, b = 1, 2
total = 0

while b <= 4000000:
    if b % 2 == 0:
        total += b
    a, b = b, a + b

print("The sum is:", total)
