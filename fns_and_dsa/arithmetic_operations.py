def perform_operation(num1, num2, operation):
  match operation:
    case 'add':
      return (num1 + num2)
    case 'subtract':
      return (num1 - num2)
    case 'multiply':
      return (num1 * num2)
    case 'divide':
      if num2 == 0:
        print('Error!!! Division by zero')
        while num2 == 0:
          num2 = float(input("Enter a number other than zero: "))
      elif num2 != 0:
        num2 = num2
      return (num1 / num2)
  
