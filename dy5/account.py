username =input(f"input your username\n")
password =input(f"input your password\n")

f = open('database.txt','r')
data = f.read()
data =eval(data)
print(data)
f.close()
if username == data["name"] and password == data["pass"]:
    print("login succesful")
else :
    print("login failed")
