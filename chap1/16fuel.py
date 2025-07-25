def main() :
    x, y = get_x_and_y("Fraction: ")
    percent = round(x/y * 100)
    if percent <= 1 :
        print("E")
    elif percent >= 99 :
        print("F")
    else :
        print(f"{percent}%")


def get_x_and_y(prompt = "prompt") :
    while True:
        try:
            s = input(prompt)
            s_parts = s.split(sep = '/')
            x = int(s_parts[0])
            y = int(s_parts[1])
        except ValueError:
            print("please enter positive integer: ")
        else :
            if y == 0:
                print("y can't be 0, please enter again: ")
                continue
            elif x > y :
                print("x can't be larger than y, please enter again: ")
                continue
            elif x < 0 or y < 0:
                print("x and y must be positive, please try again: ")
            else :
                return x, y

if __name__ == '__main__' :
    main()