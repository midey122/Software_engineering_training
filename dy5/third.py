# collect logindetails 
# read from the file 
# compare login credentials to the  one in the txt file

user_name =input(f"input username\n")
password =input(f"inputpassword\n")

# opened the file
f = open('database.txt', 'r')

# read from the file
data = f.read()

# convert the read file to python  format
data = eval(data)

f.close()
if user_name == data["name"] and password == data["pass"]:
    print("login succesful")
else :
    print("login failed")

