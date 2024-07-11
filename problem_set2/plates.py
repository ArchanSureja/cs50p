def main():
    plate = input("Plate : ")
    if is_valid(plate):
        print("Valid")
    else : 
        print("Invalid")

def is_valid(plate):
    if len(plate) < 2 or len(plate) > 6 or plate[0].isdigit() or plate[1].isdigit():
         return False
    for i in range(len(plate)-1) :
        if not plate[i].isdigit() and not plate[i].isalpha():
            return False   
    for i in range(len(plate)-1):
        if plate[i].isdigit() and plate[i+1].isalpha():
            return False
        if plate[i].isalpha() and plate[i+1]=='0' :
            return False
    return True

main()