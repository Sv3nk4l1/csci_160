# This program will store phone numbers in a directory
# The user will be able to see and search numbers

# Empty directory
contacts = {}

# Ask for the number of entries
entries = int(input('What is the number of entries you want to add: \n'))

# For loop to collect names and numbers
for number in range(entries):
    print(f'\nName {number + 1}')

    name = input('Enter a Name:\n')
    phone = input('Enter the phone number:\n')

    # Store the name and number
    contacts[name] = phone

#Display contacs
print('\n*** Direcory ***')

for name, phone in contacts.items():
    print(f'Name: {name} | Phone Number: {phone}')

# Allow search
search = input('\nEnter Name inquiry')
    # Check if name exists
if search in contacts:
    print(f'Phone number or {search}: {contacts[search]}')
else:
    print(f'Name {search} not found')