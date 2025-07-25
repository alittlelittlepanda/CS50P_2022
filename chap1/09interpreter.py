def main() :
    formula = input("please enter the formula :")
    formula_parts = formula.split()
    formula_parts[0] = float(formula_parts[0])
    formula_parts[2] = float(formula_parts[2])
    if '+' in formula :
        result = formula_parts[0] + formula_parts[2]
        print(f"{result: .1f}")
    elif '-' in formula :
        result = formula_parts[0] - formula_parts[2]
        print(f"{result: .1f}")
    elif '*' in formula :
        result = formula_parts[0] * formula_parts[2]
        print(f"{result: .1f}")
    elif '/' in formula :
        result = formula_parts[0] / formula_parts[2]
        print(f"{result: .1f}")

if __name__ == '__main__' :
    main()