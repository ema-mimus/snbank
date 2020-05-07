import json
from random import randint
data = {}  
data['customer'] = []
details = {}

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def staff():
    print("*************************************")
    print("=<< 1. Create new bank account    >>=")
    print("=<< 2. Check Account Details      >>=")
    print("=<< 3. Logout                     >>=")
    print("*************************************")
    choice = input(f'Select your choice number from the above menu :')
    if choice == "1":
        create()
    elif choice == "2":
        account()
    elif choice == "3":
        welcome()
    else:
        print('Wrong input')
        staff()

def create():
    name = input(f"Enter customer's name")
    details['name'] = name
    balance = input('Enter opening balance')
    details['balance'] = balance
    acc_type = input(f'Enter account type(Savings or Current)')
    details['acc_type'] = acc_type
    email = input('Enter email')
    details['email'] = email
    number = random_with_N_digits(10)
    details['acc_number'] = number
    data['customer'].append(details)
    with open('customer.txt', 'w') as outfile:
        json.dump(data, outfile)
    print(f"An account with account number {number} has been opened for {name}")
    staff()

def account():
    with open('customer.txt') as json_file:  
        data = json.load(json_file)
        for customer in data:
            try:
                number = int(input(f"Please enter customer's account number"))
                if number == (data[customer][0]['acc_number']):
                    print(data[customer])
                    staff()
                else:
                    print('Customer not found')
                    staff()
            except ValueError:
                print('Only integers are allowed')
                staff()
                
def exit():
    file = open('customer.txt', 'r+')
    file.truncate()
    file.close()
    print("Thank you for using our banking system!")
    
def login():
    print(f"Enter Details")
    username = input("Please enter your username")
    password = input(f'Please enter your password')
    with open('staff.txt') as json_file:  
        data = json.load(json_file)
        for p in data['staff']:
            if username == p['username'] and password == p['password']:
                print('Welcome')
                staff()
                break
            else:
                print('Username or password not found')
                login()

def welcome():
    print("=====================================")
    print("     ----Welcome to SNBank----       ")
    print("*************************************")
    print("=<< 1. Staff Login                >>=")
    print("=<< 2. Close App                  >>=")
    print("*************************************")
    choice = input(f'Select your choice number from the above menu :')
    if choice == "1":
        login()
    elif choice == "2":
        exit()
    else:
        print('Wrong input')
        welcome()

welcome()