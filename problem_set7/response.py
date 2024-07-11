import validators 
def main():
    print(is_valid_email(input("What's your email address ")))

def is_valid_email(s):
        if True == validators.email(s.strip()):
            return "Valid"
        else:
            return "Invalid"

if __name__ == "__main__":
    main()
