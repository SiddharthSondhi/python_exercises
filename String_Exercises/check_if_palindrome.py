print("Please enter a string.")

string_list = list(input())

while True:
    reversed_list = list(reversed(string_list))

    if reversed_list == string_list:
        print("Yes, it is palindrome.")
    else:
        print("No, it is not palindrome.")

    print("Enter another string or enter 'E' to exit.")

    string_list = input()

    if string_list[0] in ['E', 'e'] and len(string_list) == 1:
        break

