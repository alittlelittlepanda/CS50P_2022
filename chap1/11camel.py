def main() :
    name = input("please enter the name in camel case :")
    for _ in name :
        if 'A' <= _ <= 'Z':
            print("_"+ chr( ord(_) - ord('A') + ord('a')) , end = "")
        else :
            print(_, end = "")
    print()

if __name__ == '__main__':
    main()