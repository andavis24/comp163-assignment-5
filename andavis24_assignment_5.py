# COMP 163 - Assignment 4: College Life Adventure Game
# Author: Ajani Davis
# This program simulates college decisions using branching logic.

print("=== Challenge 1: Collatz Conjecture ===")

curent_number = int(input("Enter starting number: "))
print("Sequence: ", end="")
step_count = 0
while curent_number > 1:
    print(int(curent_number), end=" ")
    if curent_number % 2 == 0:
        curent_number = curent_number//2
    else:
        curent_number = curent_number * 3 + 1
    step_count = step_count + 1
print(int(curent_number))
print("Steps:",step_count)
print()

print("=== Challenge 2: Prime Number Checker ===")
num = int(input("Enter a number: "))
print(f"Testing divisors from 2 to {num - 1}...")

test = num - 1

while test >= 2:
    if num % test == 0:
        print(f"{num} is not prime (divisible by {test})")
        break
    else:
        test = test - 1

if test < 2:
    print(f"{num} is prime!")

print()
