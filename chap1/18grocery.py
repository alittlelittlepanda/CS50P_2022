def main() :
    grocery_list = []
    while True:
        try:
            item = input("Item: ").strip().upper()
            if item:
                grocery_list.append( item )
        except EOFError:
            break
    count = {}
    for item in grocery_list:
        count[item] = count.get(item, 0) + 1
    for item in sorted(count):
        print(f"{count[item]} {item}")

if __name__ == "__main__":
    main()
