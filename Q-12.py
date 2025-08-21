#### Q-12  / WAP to enter principle,rate and time in years and find the simple interrest

p=int(input("Enter the principle amount:"))
r=int(input("Enter rate of interest:"))
n=int(input("Enter time:"))
si=(p*n*r)/100;
print("Simple interest amount is:",si)