def main():
        greet = input()
        greet = greet.strip()
        print("Value :",value(greet))
def value(greet):

    if greet == "hello":
        return 0
    elif greet[0] == "h" or greet[0] == "H":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()