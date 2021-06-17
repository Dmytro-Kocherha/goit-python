result = None
operand = None
operator = None
wait_for_number = True
​
while True:
    
    if wait_for_number:
        wait_for_number = not(wait_for_number)
        
        try:
            operand = int(input('input operand:'))
            
        except ValueError:
            print('It\'s not a number! Try again.')
            wait_for_number = True
            continue
            
        if result == None:
            result = operand
​
        if operator == '+':
            result += operand
            
        elif operator == '-':
            result -= operand
            
        elif operator == '*':
            result *= operand
            
        elif operator == '/':
            result /= operand
            
    else:
        operator = input('input operator:')
​
        if operator != '+' and operator != '-' and operator != '*' and operator != '/' and operator != '=':
            print(operator + ' is not +, -, *, / or =. Try again!')
            wait_for_number = False
            continue
        
        if operator == '=':
            print (result)
            break
        
        wait_for_number = not(wait_for_number)
