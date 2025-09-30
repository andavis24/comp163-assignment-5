# === Challenge 1: Collatz Conjecture ===
print("=== Challenge 1: Collatz Conjecture ===")

# Ask user for a starting number
curent_number = int(input("Enter starting number: "))

# Print beginning of sequence label
print("Sequence: ", end="")

# Initialize step counter
step_count = 0

# While the number is greater than 1, keep applying Collatz rules
while curent_number > 1:
    # Print current number in the sequence
    print(int(curent_number), end=" ")

    # Rule 1: If even, divide by 2
    if curent_number % 2 == 0:
        curent_number = curent_number // 2
    # Rule 2: If odd, multiply by 3 and add 1
    else:
        curent_number = curent_number * 3 + 1

    # Count each step
    step_count = step_count + 1

# Print the final 1 when sequence ends
print(int(curent_number))

# Print total steps taken
print("Steps:", step_count)
print()  # blank line for spacing

# === Challenge 2: Prime Number Checker ===
print("=== Challenge 2: Prime Number Checker ===")

# Ask user for a number to test
num = int(input("Enter a number: "))

# Show which divisors will be tested
print(f"Testing divisors from 2 to {num - 1}...")

# Start divisor test from (num - 1) down to 2
test = num - 1

# Loop until test goes below 2
while test >= 2:
    # If number is divisible by current test value
    if num % test == 0:
        # Not prime — print explanation
        print(f"{num} is not prime (divisible by {test})")
        break  # stop checking once a divisor is found
    else:
        # Try the next smaller divisor
        test = test - 1

# If no divisors were found (test dropped below 2), it's prime
if test < 2:
    print(f"{num} is prime!")

print()  # blank line for spacing

# === Challenge 3: Multiplication Table ===
print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")

# Print header row (numbers 1–10 across the top)
print("    ", end="")  # leave space before header
for col in range(1, 11):
    print(f"{col:4}", end="")  # print each column header, spaced
print()  # move to next line

# Print each row of the table
for row in range(1, 11):
    print(f"{row:2} ", end="")  # print row label (1–10)

    # Print products for this row
    for col in range(1, 11):
        print(f"{row * col:4}", end="")  # print product with spacing

    print()  # move to next line after row finishes
