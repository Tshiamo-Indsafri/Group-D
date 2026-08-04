def Add(a:float, b:float):
    return a + b

def Sub(a:float, b:float):
    return a - b

def Mul(a:float, b:float):
    return a * b

def Div(a:float, b:float):
    if b == 0:
        return "Number can not be 0"
    else:
        return a / b


if __name__ == "__main__":
    num1 = float(input("Enter 1 number: "))
    num2 = float(input("Enter 2 number: "))

    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == "1":
        print("Result:", Add(num1, num2))
    elif choice == "2":
        print("Result:", Sub(num1, num2))
    elif choice == "3":
        print("Result:", Mul(num1, num2))
    elif choice == "4":
        print("Result:", Div(num1, num2))
    else:
        print("Invalid choice")
