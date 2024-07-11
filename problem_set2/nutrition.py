nutrition_list = [
    {"fruit":"apple","calories":130},
    {"fruit":"banana","calories":110},
    {"fruit":"grape","calories":200},
    {"fruit":"orange","calories":140},
    {"fruit":"peach","calories":150},
    {"fruit":"pear","calories":154},
]
fruit_name = input("Fruit name : ")
for i in nutrition_list:
    if i["fruit"] == fruit_name.lower():
        print("Calories : ",i["calories"])
