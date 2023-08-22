animals = {'dog', 'cat'}
print(animals)
print('='*64)

'''set.add(element)'''
# add an element to sert
animals.add('rat')
print(animals)
print('='*64)

'''set.clear()'''
# Clear all elements in the set
animals.clear()
print(animals)
print('='*64)

'''set.copy()'''
new_animals = animals.copy()
print(new_animals)
print('='*64)

'''set.difference(set)'''
# return set with items that exist only in the first set, and not in both sets
other_animals = {'lion', 'tiger', 'cat'}
search1 = other_animals.difference(animals)
print(search1)

print('='*64)

'''set.difference_update(set)'''
# inplace update set with the difference
animals = {'dog', 'cat'}
other_animals = {'lion', 'tiger', 'cat'}
animals.difference_update(other_animals)
update= other_animals.difference_update(animals)
print(update)
print('='*64)

'''set.discard(items)'''
# remove item from the set, if item is missing no error is raised
animals = {'lion', 'tiger', 'cat'}
set_discard = animals.discard('cat')
print(set_discard)
animals.discard('bat')
print('='*64)

'''set.intersection(set)'''
# return a set that contains the similary between two or more sets
other_animals = {'lion', 'tiger', 'cat'}
animals = {'lion', 'tiger', 'cow'}
inter = other_animals.intersection(animals)
print(inter)
print('='*64)

'''set.interseccion_update(set)'''
# In place update of set with common elementes
other_animals = {'lion', 'tiger', 'cat'}
animals = {'lion', 'tiger', 'cow'}
u = other_animals.intersection_update(animals)
print(u)
print('='*64)

'''set.isdisjoint(set1)'''
# returns True if no elementes in set are present in set1
other_animals = {'lion', 'tiger', 'cat'}
animals = {'lion', 'tiger', 'cow'}
another_set_of_animals = {'dino'}
a = other_animals.isdisjoint(animals)
b = other_animals.isdisjoint(another_set_of_animals)

print(a)
print(b)
print('='*64)

'''set.issubset(set1)'''
# returns True is all element in set are present in set1
other_animals = {'lion', 'tiger', 'cat'}
animals = {'lion', 'tiger', 'cow'}
another_set_of_animals = {'dino'}
c = other_animals.issubset(animals)
d = other_animals.issubset(another_set_of_animals)

print(c)
print(d)
