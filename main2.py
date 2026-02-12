my_dict = {
    'name': 'Atharva',
    'age': 14
}

print(my_dict.get('name'))
print(my_dict.get('age'))

my_dict['age'] = 15
print(my_dict)

my_dict['Favourite Colour'] = 'Blue'
print(my_dict)

my_dict.pop('age')
print(my_dict)

print('Fav Color', my_dict.get('Favourite Colour'))

my_dict.clear()
print(my_dict)

print("Updated list", my_dict)