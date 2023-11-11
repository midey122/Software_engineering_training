f = open('database.txt', 'r')
data = f.read()
data = eval(data)
for item in data:
    print(item["name"])
    print(item)

f.close()