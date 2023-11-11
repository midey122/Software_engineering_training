def calculator(num1, num2, operations):
    match operations:
        case "*":
            return num1 * num2
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "/":
            return num1 / num2
        
print(calculator(2,65,"+"))