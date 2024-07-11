month_list = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
def is_valid(date):
    if '/' in date :
        month , day , year = date.split('/')
        if int(month)>12 or int(month)<1 or int(day)>31 or int(day)<1:
            return False
        else :
            return True
    else : 
        month, day, year = date.split(" ")
        day = int(day[0])
        if month not in month_list :
            return False
        elif day<0 or day>31 :
            return False
       
    return True

def convert_date(date):
    if "/" in date :
        month , day , year = date.split('/')
    else :
        month, day, year = date.split(" ")
        day = int(day[0])
        for i in range(len(month_list)-1):
           if month_list[i] == month:
                month = i + 1
        print(f"{year}-{month}-{day}")

def main():
 while True:
      date = input("Date : ")
      if is_valid(date):
        convert_date(date)
        break

main()   