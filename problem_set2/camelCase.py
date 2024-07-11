camel_case = input("camelCase : ")
print("snake_case : ",end="")
for i in camel_case:
    if i == i.upper():
        print("_",sep="",end="")
    print(i.lower(),sep="",end="")