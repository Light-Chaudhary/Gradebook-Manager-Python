# Python Calculator

num1 = float(input("Enter the first number = "))
num2 = float(input("Enter the second number = "))

choice = int(input("=== Enter your choice === \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Remainder\n6. Exponential\n"))

if choice ==1 :
    total = num1 + num2
    print(f"Addition of {num1} and {num2} is {total}")
elif choice == 2 :
    total = num1 - num2
    print(f"Subtraction of {num1} and {num2} is {total}")
elif choice == 3 :
    total = num1 * num2
    print(f"Multiplication of {num1} and {num2} is {total}")
elif choice == 4 :
    total = num1 / num2
    print(f"Division of {num1} by {num2} is {total}")
elif choice == 5 :
    total = num1 % num2
    print(f"Remainder of {num1} by {num2} is {total}")
elif choice == 6:
    total = num1 ** num2
    print(f"Exponential of {num1}**{num2} is {total}")
else :
    print("Invalid choice")
