#SIMPLE CALCULATOR
#TASK-2
print("SIMPLE CALCULATOR")
print("---------------------------------")
print("Select operation to be performed:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

def addion(a, b):
   return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Can't divide with zero"
    return a / b

select =input("Enter choice 1,2,3,4: ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if select == '1':
    print("Add:",num1, "+", num2, "=", addion(num1, num2))
elif select == '2':
    print("Subtract:",num1, "-", num2, "=", subtract(num1, num2))
elif select == '3':
    print("Multiply:",num1, "*", num2, "=", multiply(num1, num2))
elif select == '4':
    print("Division:",num1, "/", num2, "=", divide(num1, num2))
else:
    print("Please Enter valid choice !")