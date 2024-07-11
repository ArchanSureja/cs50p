import requests 
import json
import sys 

if len(sys.argv)<2:
    print("Missing Command-Line Arguments")
elif len(sys.argv)==2:
    try:
        num = float(sys.argv[1])
    except ValueError:
        print("Command-Line Arguments is not a number")
        sys.exit(1)
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        print("Please Try again later")
        sys.exit(1)
    obj = response.json()
    p=obj["bpi"]["USD"]["rate_float"]*num
    price_final = ('{:,}'.format(p))
    print("$",price_final) 

       