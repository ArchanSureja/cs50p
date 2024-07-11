import sys 
import csv
from tabulate import tabulate
def main():
    if len(sys.argv) == 1:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2 :
        print("Too many command-line arguments")
    elif len(sys.argv)==2:
        name , extension = sys.argv[1].split(".")
        if extension != "csv":
            print("Not a CSV file")
            sys.exit(1)
    item_list = []
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            item_list.append(row)
    
    print(tabulate(item_list,tablefmt="grid"))

if __name__ == '__main__':
        main()