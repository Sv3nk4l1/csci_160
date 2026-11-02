fruits = ['papya', 'grapes', 'tomato', 'cucumber', 'jackfruit']
print(fruits)
print("First fruit:", fruits[0])
print("Third fruit:", fruits[2])
print("Last fruit:", fruits[-1])

favorite_fruit = input('What is your favorite fruit? \n')
fruits.append(favorite_fruit)
print(fruits)

fruits[1] = 'mango'
fruits.remove(fruits[4])
print(fruits)

print(len(fruits))

for fruit in fruits:
    print(fruit)

if 'apple' in fruits:
    print('apple is in the list')
else:
    print('apple is in the list')

fruits.sort()
print(fruits)