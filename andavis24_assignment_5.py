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