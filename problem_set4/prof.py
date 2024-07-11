import random
def main():
    level = get_level()
    genrated_problems = genrate_ints(level)
    i = 0
    score = 0
    error = 0
    while True:
        if i<19:
          print(genrated_problems[i],"+",genrated_problems[i+1],"= ",end="")
        else:
            print("Score : ",score)
            break
        ans = input()
        try:
            ans = int(ans)
        except ValueError:
            continue
        if ans == int(genrated_problems[i])+int(genrated_problems[i+1]):
            i+=2
            score+=1
        elif error!=2:
            print("EEE")
            error+=1
        elif error==2:
            print(genrated_problems[i],"+",genrated_problems[i+1],"= ",int(genrated_problems[i])+int(genrated_problems[i+1]))
            i+=2
        



def get_level():
    while True:
        
        level = int(input("Level : "))
        
        if level==1 or level==2 or level==3:
            return level

def genrate_ints(level):
    problems = []
    for i in range(20):
        problems.append(random.randint(0,10**level-1))
    return problems

main()
