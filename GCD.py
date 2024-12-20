#Greatest Common Divisor algorithm
    while b:
        a, b = b, a % b
    return a

print(gcd(1, 35))
print(hello)
