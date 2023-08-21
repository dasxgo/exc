import random

def main():
    def get_random_number():
        return random.randint(1,6)
    
    number = get_random_number()
    print('The number is:', number)

if __name__ == '__main__':
    main()


