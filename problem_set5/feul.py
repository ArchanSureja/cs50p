def main():
       number = input("Fraction : ")
       print(gauge(convert(number)))


def convert(fraction):
    a , b = fraction.split("/")
    a = int(a)
    b = int(b)
    if b==0 :
         raise ZeroDivisionError
    elif a>b:
        raise ValueError
    return int(100 * a/b)

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage<=1:
        return "E"
    else:
        return f"{percentage}%"
    
if __name__ == "__main__":
    main()