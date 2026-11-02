#Tuples
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(days)

print(days[0])
print(days[3])
print(days[-1])

len(days)

for day in days:
    print(day)

if 'Monday' in days:
    print('Monday is in the tuple')
else:
    print('Monday is not in the tuple')

interim = list(days)
interim[0] = 'Holiday'
days = tuple(interim)
print(days)



#Sets
colors = {'Red', 'Blue', 'Green', 'Yellow'}
print(colors)

colors.add('Purple')
colors.remove('Yellow')
favorite_color = input('What is your favorite color? \n')
colors.add(favorite_color)

for color in colors:
    print(color)

len(colors)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))