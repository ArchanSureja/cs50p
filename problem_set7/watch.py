import re
import sys

def main():
    print(parse(input("HTML : ")))

def parse(s):
    match = re.search(r"embed/([^\"']+)",s)
    if match:
        url = match.group(1)
        return "https://youtu.be/"+url
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()