question = input("what's the anser of the great question of the life ?")
match question : 
    case "42" | "forty-two" | "FORTY-TWO":
        print("yes")
    case _:
        print("no")
     