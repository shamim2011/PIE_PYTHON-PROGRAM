#### Q-07  / WAP to enter salary of a person and find HRA,DA,PF.
#           HRA= 20 % of the salary
#           DA= 15 % of the salary
#           PF=10% of the salary

salary = float(input("Enter the salary of the person: "))

# Calculate HRA, DA, and PF
HRA = 0.20 * salary
DA = 0.15 * salary
PF = 0.10 * salary

# Calculate the net salary
net_salary = salary + HRA + DA - PF
salary_inHand=net_salary+(HRA+DA+PF)
# Print the results
print("Salary=",salary)
print("HRA=", HRA)
print("DA=", DA)
print("PF=", PF)
print("Net salary=",net_salary)
print("Salary in hand=",salary_inHand)
