
name_list = []
while True:
    try:
        name = input("Name : ")
        name_list.append(name)
    except KeyboardInterrupt:
        break
        print("Adieu, adieu, to ",end="")
        for name in name_list:
            print(name,sep=" and ",end="")