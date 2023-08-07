## Country definition

def city(country):
    if country == 'Colombia':
        return 'Bogota'
    elif country == 'Brasil':
        return 'Sao Paulo'
    elif country == 'Peru':
        return 'Lima'
    elif country == 'Ecuador':
        return 'Quito'
    else:
        return 'Desconocido'

print(f'The city is =>',city('Peru'))
print('='*64)

# Map funtion

def add_list(a,b):
    return a+b

output = list(map(add_list,[2,6,3],[3,4,5]))
print(output)
print('='*64)

# Enumarate function

browsers = ['Chrome', 'Firefox', 'Opera', 'Vivaldi']

x = list(enumerate(browsers))
print(x)
print('='*64)

# Filter function

def is_positive(a):
    return a>0

output = list(filter(is_positive,[1,-2,3,-4,5,6]))
print(output)
print('='*64)

# Zip function

user_id = ['12121', '56161', '33287', '23244']
user_name = ['Mick', 'Jhon', 'Tessa', 'Nick']
user_info = (list(zip(user_name, user_id)))
print(user_info)
print('='*64)
