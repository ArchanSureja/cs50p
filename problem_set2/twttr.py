input_str = input("Input : ")
print("Output : ",end="")
for i in input_str:
    if i.lower() in ['a','e','i','o','u'] :
        continue
    else :
        print(i,sep="",end="")