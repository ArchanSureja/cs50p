import sys
import csv 

def main():

    if len(sys.argv)<3:
        sys.exit(1)
item_list =  []
try :

    with open(sys.argv[1],"r") as read_file:
       reader = csv.DictReader(read_file)
       for line in reader:
            lastname , firstname = line["name"].split(",")
            house = line["house"]
            house= house.rstrip()
            item_list.append({"firstname":firstname, "lastname":lastname, "house":house})
except FileNotFoundError:
    sys.exit(1)

with open(sys.argv[2],"a") as write_file:
    writer = csv.DictWriter(write_file,fieldnames=["firstname","lastname","house"])
    for dic in item_list:
        writer.writerow({"firstname":dic["firstname"],"lastname":dic["lastname"],"house":dic["house"]})