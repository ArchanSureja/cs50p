from datetime import date
import sys 
from datetime import date
from num2words import num2words

def main():
    birth_date = input("Date of Birth : ")
    if(is_valid(birth_date)):
        print(to_mins(birth_date),"minutes")
    else:
        print("Invalid date")
        sys.exit(1)


def is_valid(d):
    year, month, day = d.split('-')
    if not (year.isnumeric() or month.isnumeric() or day.isnumeric):
               return False
    return True
    
def to_mins(d):
    year, month, day = d.split('-')
    today = date.today()
    birth_date = date(int(year), int(month), int(day))
    diff = today - birth_date
    return num2words(diff.days * 24 * 60)
    



if __name__ == "__main__":
    main()