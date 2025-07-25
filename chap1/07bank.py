def main() :
    s = input("please greet :")
    s = s.strip()
    if s[0:5] == 'hello' or s[0:5] == 'Hello' :
        print("$0")
    elif s[0] == 'h' or s[0] == 'H' :
        print("$20")
    else :
        print("$100")

if __name__ == '__main__' :
    main()