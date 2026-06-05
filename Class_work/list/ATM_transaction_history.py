# List of transactions
transactions = [5000, -2000, 3000, -1000, -500, 7000]

# Separate lists for deposits and withdrawals
deposits = []
withdrawals = []

# Current balance
balance = 0

# Find deposits and withdrawals
for amount in transactions:
    balance += amount

    if amount > 0:
        deposits.append(amount)
    else:
        withdrawals.append(amount)

# Count deposits and withdrawals
deposit_count = len(deposits)
withdrawal_count = len(withdrawals)

# Find largest deposit and largest withdrawal
largest_deposit = deposits[0]
for amount in deposits:
    if amount > largest_deposit:
        largest_deposit = amount

largest_withdrawal = withdrawals[0]
for amount in withdrawals:
    if amount < largest_withdrawal:
        largest_withdrawal = amount

# Display results
print("Current Balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Total Deposits:", deposit_count)
print("Total Withdrawals:", withdrawal_count)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)