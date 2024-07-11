expression = input("expression: ")
length = len(expression)

idx = expression.find(" ")
digit1 = int(expression[0:idx])
print(digit1)
idx = expression.find(" ",idx+1,length-1)
digit2 = expression[idx+1:length-1]
print(digit2)
digit1 = int(digit1)
digit2 = int(digit2)
if "+" in expression:
    print(float(digit1 + digit2))
elif "-" in expression:
    print(float(digit1 - digit2))
elif "*" in expression:
    print(float(digit1 * digit2))
elif "/" in expression:
    print(float(digit1 / digit2))
else :
    print("invalid operator")