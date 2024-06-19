

def add(num1 , num2):
    print(f"{num1} + {num2} = {num1 + num2}")
    return num1 + num2

def sub(num1 , num2):
    print(f"{num1} - {num2} = {num1 - num2}")
    return num1 - num2

def mul(num1 , num2):
    print(f"{num1} * {num2} = {num1 * num2}")
    return num1 * num2

def div(num1 , num2):
    print(f"{num1} / {num2} = {num1 / num2}")
    return num1 / num2


def run_calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        add(num1 , num2)

    elif choice == '2':
        sub(num1 , num2)

    elif choice == '3':
        mul(num1 , num2)

    elif choice == '4':
        div(num1 , num2)

    else:
        print("Invalid input")

run_calculator()