for i in range(10):
    number1= input(f"input your number\n")
    number2= input(f"input your number\n")

    number1 =int(number1)
    number2 =int(number2)
    operation = input (f"input your operation\n") 
    if operation == "add":
        print(number1 + number2)
    else :
        print("operation failed")