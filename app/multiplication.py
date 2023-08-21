def get_number():
    while True:
        try:
            number = int(input('Enter an integer number: '))
            return number
        except ValueError:
            print('invalid value Please enter a valid integer')

def view_multiplication_table(number):
    print('The multiplication table is {number}:')
    for i in range(1,50):
        result = number * i
        print(f'(number) * {i} = {result}')

def main():
    print('Welcome to the multiplication table')
    number = get_number()
    view_multiplication_table(number)

if __name__ == '__main__':
    main()




