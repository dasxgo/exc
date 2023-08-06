animals = ['cat', 'dog']

'''list.index(element, start, end)'''
# start and end are optional
# get the infex of 'dog' or value error

animals.index('dog')
animals.index('dog', 0, 3)

print(animals)


print('='*64)

'''list.append(item)'''
# an item (number, string, liest, etc) to be added
# at the end the list


'''list.append(item)'''
animals.append('hen')
print(animals)

print('='*64)

'''list.extend(iterable)'''

print(animals.extend(['duck', 'mouse']))
print(animals)

print('='*64)

'''list insert(i, elemnet)'''
# element is insert to the list at the ith index

animals.insert(0, 'rat')
print(f'animals =>',animals)

print('='*64)

'''list.remove(element)'''
# remove element or return ValueError if element not found

animals.remove('rat')
print(animals)

print('='*64)

'''list.count(element)'''

print(animals.count('dog'))

print('='*64)

'''list.pop(index)'''
# Remove item at the give index from the list & return the removed item
# Index is optional & default value is -1 i.e. last element

print(animals.pop())
print(animals.pop(0))
print(animals)

print('='*64)

'''list.revese()'''
# Reverse tthe list in place

animals.reverse()
print(animals)

print('='*64)

'''list.sort(key=..., reverse=...)'''
# Sort list inplace
# if reverse = True sort in descending order
# key = funtion that serves as a key for the comparison

animals.sort()
print(animals)

print('='*64)

'''list.copy()'''
# copu list to a new list, a new list is created & not just a reterece

new_animals = animals.copy()
print(new_animals)

print('='*64)

''' list.clear()'''
# Empty the list

new_animals.clear()
print(new_animals)