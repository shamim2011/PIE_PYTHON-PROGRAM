#### Q-20  / WAP to swap the values of two variable using third variable

# Taking input two variables
var1 = int(input("Enter the value of the first variable: "))
var2 = int(input("Enter the value of the second variable: "))

# Swap the values using a third variable
temp = var1
var1 = var2
var2 = temp

# Print the swapped values
print("After swapping:")
print("First variable:", var1)
print("Second variable:", var2)