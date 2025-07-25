def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if start_with_2_letters(s) and 2 <= len(s) <= 6 and no_special_sign(s) and end_with_num(s) and not(number_start_with_0(s)):
                    return True
    else :
        return False
        
    
def start_with_2_letters(s) :
    if len(s) <= 2 :
        return False
    if 'A' <= s[0] <= 'Z' and 'A' <= s[1] <= 'Z' :
        return True
    else :
        return False

def no_special_sign(s) :
    for _ in s :
        if not ('A' <= _ <= 'Z' or '0' <= _ <= '9') :
            return False
    return True 

def end_with_num(s) :
    flag = 0
    for _ in s :
        if '0' <= _ <= '9' :
            flag = 1
        elif flag == 1 and 'A' <= _ <= 'Z' :
            return False
    return True 

def number_start_with_0(s) :
    count = 0
    for _ in s :
        if '0' <= _ <= '9' :
            count += 1
        if count == 1 and _ == '0' :
            return True
    return False

if __name__ == '__main__' :
    main()