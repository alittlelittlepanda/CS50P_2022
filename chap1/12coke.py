def main() :
    amount_due = 50
    while amount_due > 0 :
        print("Amount Due :", amount_due)
        insert_coin = int(input("insert coin :"))
        if insert_coin == 25 or insert_coin == 10 or insert_coin == 5 :
            amount_due -= insert_coin
    print("Change Owed :", -amount_due)

if __name__ == '__main__' :
    main()
