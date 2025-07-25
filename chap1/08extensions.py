def main() :
    name = input("please enter the file name with extension :")
    name = name.strip()
    if ".gif" in name :
        print("image/gif")
    elif ".jpg" in name or ".jpeg" in name :
        print("image/jpeg")
    elif ".png" in name :
        print("image/png")
    elif ".pdf" in name :
        print("application/pdf")
    elif ".txt" in name :
        print("text/plain")
    elif ".zip" in name :
        print("application/zip")
    else :
        print("application/octet-stream")

if __name__ == "__main__" :
    main()