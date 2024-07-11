amount_due = 50

while True : 
    print("Amount Due : ",amount_due)
    inserted_coin=int(input("Insert Coin : "))
    if inserted_coin not in [25,10,5] :
        continue
    else:
       amount_due -= inserted_coin
       if amount_due <= 0 :
            print("change owed : ",abs(amount_due))
            break 
    
