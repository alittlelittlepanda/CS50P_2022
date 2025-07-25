def main() :
    s = input("please enter the sentence :")
    for _ in s :
        for omitted in ['a','e','i','o','u','A','E','I','O','U'] :
            if _ == omitted :
                break
        else : 
            print(_, end = "")
    print()           

if __name__ == '__main__' :
    main()