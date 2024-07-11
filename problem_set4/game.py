import random 

while True:
    level = input("Level : ")
    if level.isdigit() and int(level) > 0:
        break
while True:
    num = random.randint(1,int(level))
    guess = int(input("Guess : "))
    if guess < num :
        print("Too small!")
    elif guess > num :
        print("Too big!")
    else:
        print("just right!")
        break