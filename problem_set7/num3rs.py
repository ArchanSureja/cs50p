import re
def main():
    print(validate(input("IPv4 Address: ").rstrip()))

def validate(ip):
    match = re.search(r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$",ip)
    if match:
        return "ip is valid"
    else:
        return "ip is not valid"

if __name__ == "__main__":
    main()