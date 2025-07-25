nutrition_dict = [
    {"Fruits" : "Apple", "Calories" : "130"},
    {"Fruits" : "Avocado", "Calories" : "50"},
    {"Fruits": "Banana", "Calories": "110"},
    {"Fruits": "Cantaloupe", "Calories": "50"},
    {"Fruits": "Grapefruit", "Calories": "60"},
    {"Fruits": "Grapes", "Calories": "90"},
    {"Fruits": "Honeydew Melon", "Calories": "50"},
    {"Fruits": "Kiwifruit", "Calories": "90"},
    {"Fruits": "Lemon", "Calories": "15"},
    {"Fruits": "Lime", "Calories": "20"},
    {"Fruits": "Nectarine", "Calories": "60"},
    {"Fruits": "Orange", "Calories": "80"},
    {"Fruits": "Peach", "Calories": "60"},
    {"Fruits": "Pear", "Calories": "100"},
    {"Fruits": "Pineapple", "Calories": "50"},
    {"Fruits": "Plums", "Calories": "70"},
    {"Fruits": "Strawberries", "Calories": "50"},
    {"Fruits": "Sweet Cherries", "Calories": "100"},
    {"Fruits": "Tangerine", "Calories": "50"},
    {"Fruits": "Watermelon", "Calories": "80"},
]

def main() :
    fruit = input("Item: ").capitalize()
    for item in nutrition_dict:
        if fruit == item["Fruits"] :
            print("Calories: ", item["Calories"])

if __name__ == '__main__' :
    main()