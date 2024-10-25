import random 
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
           'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
print("Welcome To Password Generator")
print("*"*30)
no_of_letters=int(input("How many letters do you want to in your password\n"))
no_of_numbers=int(input("How many numbers do you want to in your password\n"))
no_of_symbols=int(input("How many symbols do you want to in your password\n"))
password=[]
for i in range(no_of_letters):
    r=random.choice(letters)
    password+=r
for i in range(no_of_numbers):
    r=random.choice(numbers)
    password+=r
for i in range(no_of_symbols):
    r=random.choice(symbols)
    password+=r 
random.shuffle(password)
Password=''
for i in password:
    Password+=i
print(f"Your Password Is : {Password}")    
      
