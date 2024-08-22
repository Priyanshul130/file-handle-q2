'''def the fucntion to store and display the record in bank.txt file with record 
also def a func to search and display 
only those account details whose balance is more then 50,000'''

f = open("bank.txt", "a+")

def insert_data():
    account_number = input("Enter account number: ")
    print()
    
    name = input("Enter name: ")
    print()
    balance = input("Enter balance: ")
    print()
    f.write(f"{account_number},{name},{balance}\n")
    f.flush()
    print("Record inserted successfully")
    

def bal_search():

    f.seek(0)
    min_balance = float(input("Enter minimum balance to search: "))
    print()
    print(f"\nSearching for accounts with balance >= {min_balance}:")
    for line in f:
        account_number, name, balance = line.strip().split(",")
        if float(balance) >= min_balance:
            print(f"Account Number: {account_number}, Name: {name}, Balance: {balance}")
print()
while True:
    print("1. Insert Data")
    print("2. Balance search")
    print("3. Exit")
    print()
    choice = input("Enter your choice: ")
    if choice == "1":
        insert_data()
    elif choice == "2":
        bal_search()
    elif choice == "3":
        break
    else:
        print("Choose from 1,2,3 only")
f.close() 