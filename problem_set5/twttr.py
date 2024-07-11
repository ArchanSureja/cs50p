def main():
    input_str = input("Input : ")
    print("Output :",shorten(input_str))

def shorten(word):
    shorten_word = ""
    for i in word:
        if i.lower() in ['a','e','i','o','u'] :
            continue
        else :
            shorten_word += i
    return shorten_word

if __name__ == "__main__":
    main()