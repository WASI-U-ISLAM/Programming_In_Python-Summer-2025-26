prime_sum = 0

for num in range(2, 1000):
    is_prime = True
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        prime_sum += num

print(f"The sum of all prime numbers below 1000 is: {prime_sum}")