returnedDate, returnedMonth, returnedYear = [int(x) for x in input().split()]
dueDate, dueMonth, dueYear = [int(x) for x in input().split()]
fine = 0

if returnedYear > dueYear:
    fine = 10000
elif returnedMonth > dueMonth and returnedYear == dueYear:
    fine = (returnedMonth - dueMonth) * 500
elif returnedDate > dueDate and returnedMonth == dueMonth:
    fine = (returnedDate - dueDate) * 15

print(fine)