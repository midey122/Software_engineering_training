    #python script for a water vending machine
def vending_machine() :
    name =input(f"what is your name\n")
    print("1 bag of water is $10")
    quantity_water =input(f"quantity of water needed\n") 
    customer_price =input(f"how much are you paying\n $")
    quantity_water = int(quantity_water)
    new_price = quantity_water * 10
    customer_price = int(customer_price)

    change = customer_price - new_price
    print(f"${change}")

vending_machine()