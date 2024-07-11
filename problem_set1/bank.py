greet = input()
greet = greet.strip()
if greet == "hello":
    print("$0")
elif greet[0] == "h" or greet[0] == "H":
    print("$20")
else:
    print("$100")
