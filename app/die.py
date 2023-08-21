import random

def get_random_number():
    return random.randint(1,6)

if __name__ == '__main__':
    number = get_random_number()
    print('The number is:', number)



