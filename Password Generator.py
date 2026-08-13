import random

def generate_password(pass_length,char_list):
    password = ''
    for i in range (pass_length):
        random_index = random.randint(0,int(len(char_list))-1)
        password += char_list[random_index]
    print(password)

include_alpha = False
include_all = False
include_numbers = False
include_symbols = False

list_alpha = list("abcdefghijklmnopqrstuvwxyz")
list_alphabet_numbers = list("1234567890abcdefghijklmnopqrstuvwxyz")
list_all = list("1234567890abcdefghijklmnopqrstuvwxyz!@#$%&")
list_alphabet_symbols = list("abcdefghijklmnopqrstuvwxyz!@#$%&")
length = None

print("--------------------------------------------")
print("Welcome to Random Password Generator program")
print("--------------------------------------------")
while True:
    try:
        length = int(input('Enter length of password: '))
        break
    except ValueError:
        print('Invalid input, try again.....')

print("--------------------------------------------")
num_check = input('Include numbers? (y/n): ')
print("--------------------------------------------")
symbol_check = input('Include symbols? (y/n): ')
print("--------------------------------------------")

if num_check.lower() == 'y' and symbol_check.lower() == 'y':
    include_all = True
elif num_check.lower() != 'y' and symbol_check.lower() == 'y':
    include_symbols = True
elif num_check.lower() == 'y' and symbol_check.lower() != 'y':
    include_numbers = True
else:
    include_alpha = True

if include_all:
    print('Your password is: ')
    print("--------------------------------------------")
    generate_password(length, list_all)
elif include_symbols:
    print('Your password is: ')
    print("--------------------------------------------")
    generate_password(length, list_alphabet_symbols)
elif include_numbers:
    print('Your password is: ')
    print("--------------------------------------------")
    generate_password(length, list_alphabet_numbers)
elif include_alpha:
    print('Your password is: ')
    print("--------------------------------------------")
    generate_password(length, list_alpha)
else:
    pass

