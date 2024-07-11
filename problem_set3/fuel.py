while True:
    number = input("Fraction : ")
    a , b = number.split("/")
    try :
        a = int(a)
        b = int(b)
        percentage = (100 * a/b)
        break
    except (ValueError,ZeroDivisionError):
        pass


if percentage >= 99:
    print("F")
elif percentage <= 1:
    print("E")
else:
    print(f"{percentage:.1f}%")
    