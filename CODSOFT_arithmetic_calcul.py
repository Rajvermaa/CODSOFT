num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
n = int(
    input(
        (
            """Which operation you want to perfom?
       Press 1 for addition
       Press 2 for subtraction
       Press 3 for multiplication
       Press 4 for division
       Press 5 for modulus or remainder
       Press 6 for exponential
       Press 7 for floor division \n """
        )
    )
)


if n == 1:
    print("The sum is: ", num1 + num2)
elif n == 2:
    print("The subtraction is: ", num1 - num2)
elif n == 3:
    print("The multiply is: ", num1 * num2)
elif n == 4:
    print("The divide is: ", num1 / num2)
elif n == 5:
    print("The modulus is: ", num1 % num2)
elif n == 6:
    print("The exponential is: ", num1**num2)
elif n == 7:
    print("The floor division is: ", num1 // num2)
else:
    print("you have choose a wrong option to perform")
