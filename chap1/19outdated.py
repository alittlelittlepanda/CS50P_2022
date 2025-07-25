def main():
    month = {
        "January" : 1,
        "February" : 2,
        "March" : 3,
        "April" : 4,
        "May" : 5,
        "June" : 6,
        "July" : 7,
        "August" : 8,
        "September" : 9,
        "October" : 10,
        "November" : 11,
        "December" : 12
    }
    while True:
        date = input("Date: ")
        try:
            date_parts = date.split(sep = '/')
            for _ in range(3):
                date_parts[_] = int(date_parts[_])
            break
        except (ValueError,KeyError):
            try:
                date = date.replace(",", "")
                date_parts = date.split(" ")
                date_parts[0] = month[date_parts[0]]
                for _ in range(1,3):
                    date_parts[_] = int(date_parts[_])
                break
            except (ValueError,KeyError):
                continue
    print(f"{date_parts[2]}-{date_parts[0]:02d}-{date_parts[1]:02d}")

if __name__ == "__main__":
    main()