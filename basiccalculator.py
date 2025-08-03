# This is a simple calculator created as part of my Python learning assignment

# Asking the user to enter the first number
first_number = float(input("Enter the first number: "))

# Asking the user to enter the second number
second_number = float(input("Enter the second number: "))

# Asking the user to choose an operation
operation = input("Choose an operator (+, -, *, /): ")

# Now performing the calculation based on what the user chose
if operation == "+":
    answer = first_number + second_number
elif operation == "-":
    answer = first_number - second_number
elif operation == "*":
    answer = first_number * second_number
elif operation == "/":
    if second_number != 0:
        answer = first_number / second_number
    else:
        answer = "Math Error: Cannot divide by zero"
else:
    answer = "Invalid operator! Please use +, -, * or /"

# Showing the result to the user
if isinstance(answer, (int, float)):
    print(f"Result: {first_number} {operation} {second_number} = {answer}")
else:
    print(answer)
