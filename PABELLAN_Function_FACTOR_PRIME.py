def smallest_factor(n):
    if n < 2:
        return None
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


while True:
    print("Select an option:")
    print("1. Find the smallest factor of n")
    print("2. Find prime numbers within a range")
    print("Enter 0 to terminate")

    choice = int(input())

    if choice == 0:
        print("Program terminated.")
        break
    elif choice == 1:
        n = int(input("Enter a number to find its smallest factor: "))
        result = smallest_factor(n)
        if result is not None:
            print(f"The smallest factor of {n} is: {result}")
        else:
            print(f"{n} is less than 2.")
    elif choice == 2:
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))

        if start < 0:
            print("Enter a non-negative number for the starting point.")
            continue

        if end <= start:
            print("Enter a number greater than the starting number for the ending point.")
            continue

        print(f"Prime numbers between {start} and {end}:")

        for num in range(start, end + 1):
            if is_prime(num):
                print(num)
    else:
        print("Invalid choice. Please select 1, 2, or 0 to terminate.")
