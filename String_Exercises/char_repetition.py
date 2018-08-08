print("Please enter a string.")

string = input()

while True:
    character_dict = {}

    for character in string:
        character_dict.update({character: string.count(character)})

    if " " in character_dict:
        del character_dict[" "]

    print(character_dict)

    print("Enter another string or enter 'E' to exit.")

    string = input()

    if string in ['E', 'e']:
        break
