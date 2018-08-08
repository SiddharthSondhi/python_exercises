print("Please enter a string.")
string_list = list(input())

while True:

    string_list.reverse()

    print("This is your string reversed:", "".join(string_list))

    print("Enter another string that you would like to reverse or enter 'E' to exit.")

    string_list = list(input())

    if string_list[0] in ['E', 'e'] and len(string_list) == 1:
        break
