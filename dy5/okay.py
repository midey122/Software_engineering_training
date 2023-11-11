username = input(f"input username\n")
password = input(f"input password\n")
database =[]

try:
    f= open('database.txt', 'r+')
    database = f.read()
    database = eval(database)
    print(database)
    f.close()
    
except Exception:
        f= open('database.txt', 'w')

def create_account(username,password):
    data ={}
    data["name"] = username
    data["pass"] = password

    database.append(data)
    f = open('database.txt','w')
    f.write(str(database))
    f.close()

create_account(username,password)