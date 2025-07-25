happy_face = "\U0001F642"
sad_face = "\U0001F614"

def main() :
    s = input("请输入一段含有表情的文字：")
    s = s.replace(":)", happy_face)
    s = s.replace(":(", sad_face)
    print(s)

if __name__ == "__main__":
    main()