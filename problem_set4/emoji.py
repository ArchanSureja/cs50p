emoji_dict = {
    ":smile:": "😊",
    ":laugh:": "😂",
    ":celebrate:": "🎉",
    ":cool:": "😎",
    ":star:": "🌟",
    ":fire:": "🔥",
    ":hundred:": "💯",
    ":party:": "🥳",
    ":clap:": "👏",
    ":heart:": "💖"
}

input_str = input("Input : ")
list_str = input_str.split(" ")

print(list_str)   

for i in range(len(list_str)-1):
    if list_str[i] in emoji_dict:
        list_str[i]=emoji_dict[list_str[i]]

for i in list_str:
   print(f'{i} ',end="")

          
