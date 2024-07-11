grocery_list = {}

def add_item(item):
    if item.upper() not in grocery_list:
        grocery_list[item.upper()] = 1
    else:
        grocery_list[item.upper()] += 1

def print_list(grocery_list):
    for item in grocery_list:
        print(grocery_list[item],item)


def main():
    while True:
        try:
            item = input()
        except KeyboardInterrupt:
            print_list(grocery_list)
            break
        else:
            item.strip()
            add_item(item)

main()