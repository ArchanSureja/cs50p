import sys
from PIL import Image
from PIL import ImageOps
def main():
    if len(sys.argv) == 3:
        img1 , img2 = sys.argv[1:]
        img1, ex1 = img1.split(".")
        img2, ex2=img2.split(".")
        if ex1.lower() and ex2.lower() in ["jpeg","png","jpg"]:
            if ex1.lower() == ex2.lower():
                convert_img()
            else:
                print("Input and Ouput have different extension")
                sys.exit(1)
        else:
            print("Invalid input")
            sys.exit(1)
    elif len(sys.argv) < 3:
        print("Too few command line arguments")
        sys.exit(1)
    else:
        print("Too many command line arguments")
        sys.exit(1)

def convert_img():
    try:
        photo = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    fit =ImageOps.fit(photo, size)
    fit.paste(shirt, shirt)
    fit.save(sys.argv[2])

if __name__ == "__main__":
    main()
