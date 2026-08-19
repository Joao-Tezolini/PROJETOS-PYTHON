from art import logo
print(logo)

# TODO-1: Write out the other 3 functions - subtract, multiply and divide.

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO-2: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

# operations = {}
#
# operations[add] = "+"
# operations[subtract] = "-"
# operations[multiply] = "*"
# operations[divide] = "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# TODO-3: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
# print(operations["*"](4, 8))


f_number = float(input("Please enter the first number: "))
operator = input("Please choose one operation of the following:\n'+'\n'-'\n'*'\n'/'\n")
s_number = float(input("Please enter the second number: "))

result = operations[operator](f_number, s_number)
print(f"{f_number} {operator} {s_number} = {result}")

keep_going = True

keep_going = input("Do you want to keep going? ").lower()

if keep_going == "yes":
    keep_going = True
else:
    keep_going = False


while keep_going:
    keep_result = input(f"Do you want to use the result of the previous operation ({result}) as the first number of the next operation?: "
                        f"Type Yes or No: ").lower()
    if keep_result == "yes":
        aux_operator = input("Please choose one operation of the following:\n'+'\n'-'\n'*'\n'/'\n")
        aux_s_number = float(input("Please enter the second number: "))
        aux_result = float(operations[aux_operator](result, aux_s_number))
        print(f"{result} {aux_operator} {aux_s_number} = {aux_result}")
        result = aux_result

    elif keep_result == "no":
        f_number = float(input("Please enter the first number: "))
        operator = input("Please choose one operation oif the following:\n'+'\n'-'\n'*'\n'/'\n")
        s_number = float(input("Please enter the second number: "))

        result = operations[operator](f_number, s_number)
        print(result)

    keep_going = input("Do you want to keep going? ").lower()

    if keep_going == "yes":
        keep_going = True
    else:
        keep_going = False










