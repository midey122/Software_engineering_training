# number = {'1'}
# name = "shade"
# class_ = "ss1"
# age = "10"
# print(f'{name} is {age} years old and she is in {"ss1"}')
# # number 1 : shade is 10 years old and is in ss1
# # print("number {}  is a good number".format(number,age,))
# print("{} is {} years old and she is in {}".format(name, age ,class_))

reponse = True
trails = 0
while reponse == True:
    data_base = {
    "username":"olajide",
    "password":"1234"
    }
    user_name = input(f"username or email\n")
    password = input(f" please input your password \n")


    if user_name == data_base["username"] and password == data_base["password"]:
       print("login successful" )
       reponse = False
    elif user_name == data_base["username"] and password != data_base["password"]:
       print("incorrect password")
    elif password == data_base["password"] and user_name != data_base["username"]:
       print("incorrect username")
    else :
       print( "login failed try again")
    trails = trails + 1
    if trails == 3:
       reponse  = False
