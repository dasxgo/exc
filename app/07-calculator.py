# define the calculator funtion
def calculator():
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    operation = input('Choice an operation (+, -, *, /): ')
    
    # perform the selected operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else: 
        print('Ivalid operation selected')
        return
    print(f'The result is =>', result)

# call the calculator funtion
calculator()
    