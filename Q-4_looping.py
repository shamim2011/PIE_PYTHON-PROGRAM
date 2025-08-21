#### WAP to input a number and print factorial of a number

# Taking input the number
num = int(input("Enter a number: "))

# Initialize the factorial to 1
factorial = 1


for i in range(1, num + 1):
    factorial =factorial* i

print("The factorial of",num, "is:",factorial)