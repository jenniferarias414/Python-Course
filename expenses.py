# expenses = [10.50, 8, 9.99, 5, 15, 3.75]

# sum = 0

# for exp in expenses:
#     sum = sum + exp

# print("You spent", sum)
# print("you spent " + str(sum))
# print("You spent $", sum)
# print("You spent $", sum, sep = "")

# same problem as above but using sum function for lists

expensesList = [11.23, 54.01, 6, 20.99]

total = sum(expensesList)

print("You spent $", total, sep = "")

range(7) # 0, 1, 2, 3, 4, 5, 6
range(0, 7, 1) # 0, 1, 2, 3, 4, 5, 6
range(2, 14, 2) # start, stop, step       2, 4, 6, 8, 10, 12



total = 0
expenses = []
for i in range(7):
    expenses.append(float(input("Enter an expense: ")))

total = sum(expenses)

print("You spent $", total, sep="")



# what if we want the user to input a specific number of expenses...not just 7?

num_expenses = int(input("Enter # of expenses:"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)

print("You spent $", total, sep="")