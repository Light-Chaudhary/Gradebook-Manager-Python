# Python Calculator with History

History =[]

choice = input("Enter Y to enter program")

while choice == "y" or choice == "Y" :
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    choice_= int(input("Enter a choice for operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n"))

    if choice_ == 1 :
        total = num1 + num2
        print(total)
        History.append(f"{num1} + {num2} = {total}")
    elif choice_ == 2 :
        total = num1 - num2 
        print (total)
        History.append(f"{num1} - {num2} = {total}")
    elif choice_ == 3 :
        total = num1 * num2
        print(total)
        History.append(f"{num1} * {num2} = {total}")
    elif choice_ == 4:
        if num2 == 0 :
            continue
        total = num1 / num2 
        print(total)
        History.append(f"{num1} / {num2} = {total}")
    else :
        print("Invalid")
    choice = input("Enter Y to repeat again")
print(History)


