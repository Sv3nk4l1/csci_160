number = int(input('enter a number: \n'))

if number > 0:
    print('Positive')
elif number < 0:
    print('Negative')
else:
    print('Zero')

age = int(input('Enter your age: \n'))

if age >= 18:
    print('18 or older')
else:
    print('Under 18')

num2 = int(input('enter a number between 1 and 3: \n'))

if num2 == 1:
    print('1')
elif num2 == 2:
    print('2')
elif num2 == 3:
    print('3')
else:
    print('outside the range')