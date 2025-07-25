def main() :
    time = input("please enter the time now :")
    hour = convert(time)
    if 7 <= hour <= 8 :
        print("breakfast time")
    elif 12 <= hour <= 13 :
        print("lunch time")
    elif 18 <= hour <= 19 :
        print("dinner time")

def convert(time) :
    if "a.m." in time :
        time = time.replace("a.m.","")
        time_parts = time.split(":")
        hour = int(time_parts[0]) + float(time_parts[1])/60
    elif "p.m." in time :
        time = time.replace("p.m.","")
        time_parts = time.split(":")
        hour = int(time_parts[0]) + 12 + float(time_parts[1]) / 60
    return hour

if __name__ == '__main__' :
    main()