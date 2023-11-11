
# with open ("name.txt",'x',encoding='utf-8') as f:
#     f.write("shade")
#     f.close
# obj = (f"this is my secial file \n and this is the second line")
f = open('bid.txt', 'r')
print(f.read(200))
f.close()
