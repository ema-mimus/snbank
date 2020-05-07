# snbank - This is a solution to the task below

Python Task 4: Getting Started with Banking System with FileSystem
Your task is to create a basic banking system that stores data using the Python File System. 

1. Create a file in your project called staff.txt
2. Create a file in your project called customer.txt
  The staff.txt should contain 2 staff details
  The staff details should be the following:
    a. Username
    b. Password
    c. Email
    d. Full Name
  the customer.txt should be empty
  Implement the following:

3. On run, the program should present the following options:

  a Staff Login

  b Close App

  If the user selects Login, the user should be asked for their username and password, the program should check the pre-defined staff in a file called staff.txt and verify that the username and password are correct. If incorrect, user should see an error message and told to try again. 

  After user login is successful, a new file should be created to store the user session.

 4. After login, staff should be presented with the following options: 

  a Create new bank account

  b Check Account Details

  c Logout

  If staff selects Create bank account, 

  staff should be made to supply the following

  i. Account name

  ii. Opening Balance

  iii. Account Type

  iv. Account email

  The details above should be saved in the customer.txt file, before saving, generate a 10 digits account number for the customer.

  After staff completes creating the account, they should see the account number, and then presented with the options in (4) above.

  If Staff selects check account details from (4) above, the program should request for account number

  The program should fetch the details of the account from the customer.txt file and display it to the staff, then present back the options in (4) above.

  If staff selects logout in (4) above, delete the user session file and return the user back to the staff login page.

 

And finally, if staff selects Close App, the program should terminate.
