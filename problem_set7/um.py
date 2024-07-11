import re 
import sys

def main():
    print(count(input("Text : ")))

def count(s):
    pattern = r'.[um].'
    match = re.findall(pattern,s)
    return len(match)

if __name__ == "__main__":
    main()