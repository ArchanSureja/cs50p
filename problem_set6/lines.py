import sys

def main():
    count = 0
    name , extension = sys.argv[1].split(".")
    print(name,extension)
    if extension != "py" :
        sys.exit(1)

    try:
        print(sys.argv[1])
        with open(sys.argv[1]) as file:
            lines = file.readlines()
    except (FileNotFoundError, IOError):
        sys.exit(1)

    for line in lines:
        line = line.strip()
        if len(line)==0 or line[0]=='#':
            continue
        else:
            count+=1
    print(count)

if __name__ == "__main__":
    main()