# 1. get the user details
# 2. contert "typecast" if neccesary
# 3save it to a dicionary 
# write it into a file 


username = input(f"put in your username :\n")
password = input(f"put in your password :\n")

def create_account(username,password):
    database =[]
    data ={}
    data["name"] = username
    data["pass"] = password

    database.append(data)
    f = open('database.txt','a')
    f.write(str(database))
    f.close()


create_account(username,password)
