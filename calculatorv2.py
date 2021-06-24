import math as mt

print("Welcome to my simple Calculator. \n Operators: \n + : Addition \n - : Substraction \n * : Multiplication \n / : Division \n ^ : Raised to the Power of \n sqrt : Square Root")

def obtain_values():
    num1 = float(input("First number: "))
    op = input("Operator: ")
    if op == "sqrt":
        return num1, op
    else:
        num2 = float(input("Second number: "))
        return num1, op, num2

def operations(values):
    if values[1] == "+":
        return addition(values[0], values[2])
    elif values[1] == "-":
        return subtraction(values[0], values[2])
    elif values[1] == "+":
        return multiplication(values[0], values[2])
    elif values[1] == "-":
        return division(values[0], values[2])
    elif values[1] == "^":
        return power(values[0], values[2])
    elif values[1] == "sqrt":
        return sqroot(values[0])
    else:
        print("Invalid Operator")

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def power(num1, num2):
    return mt.pow(num1, num2)

def sqroot(num1):
    return mt.sqrt(num1)

values = obtain_values()
print(operations(values))
