# Getting user input
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
operation = input('Choose the operation (+, -, *, /): ')

# Execution based on user input
match operation:
  case '+':
    result = num1 + num2
  case '-':
    result = num1 - num2
  case '*':
    result = num1 * num2
  case '/':
    if num2 == 0:
      print('Division by zero!')
      break
    result = num1 / num2

# Displaying the result
print(f'The result is {result}')
