num1 = float(input("Enter first number:" ))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == "+":
    print=( num1 + num2)
elif op == "-":
    print( num1 - num2)
elif op == "*":
    print( num1 * num2)
elif op == "/":
    if num2 == 0:
        print("cant divide by 0")
    else:
        print("answer is:", num1 / num2)
else:
    print("not a true operation")