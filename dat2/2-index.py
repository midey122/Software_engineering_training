# a machine that sells available items 

name = input(f"input your name\n ")

available_item = ["water", "Food", "drinks"]

ordered_food = input(f"welcome {name} \n we offer only {available_item[0]} \n, {available_item[1]}\n, {available_item[2]}\n please input your choice : \n ")


if ordered_food == "water":
    print("we know you are thirsty have some water")
elif ordered_food == "food":
    print("we know you are hungry have some food")
elif ordered_food == "drinks":
    print("we know you are thirsty have some drink")
else :
    print(f"we don not have {ordered_food}")