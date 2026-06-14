max_limit = int(input("Enter the upper limit N: "))
first_term, second_term = 0, 1

print(f"Fibonacci numbers below {max_limit}:")
while first_term < max_limit:
    print(first_term, end=" ")
    first_term, second_term = second_term, first_term + second_term
print() 