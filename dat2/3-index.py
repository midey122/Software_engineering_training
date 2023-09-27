Number = input("your number")
Number = int(Number)

if Number % 2 == 0:
    print(f"{Number} is an even number")
elif Number % 3 == 0:
    print(f"{Number} is an odd number")
elif Number % 5 == 0:
    print(f"{Number} is an multiple of five")
else: 
    print("is a prime number")