print("Please enter a string. (Don't enter any extra spaces.)")

string = input()

while True:
    number_of_words = string.count(" ")

    if number_of_words > 1:
        print("There are", 1+number_of_words, "words in the string that you entered.")
    elif number_of_words == 1:
        print("There is 1 word in the string that you entered"
              ".")
    elif number_of_words == 0:
        print("You hav not entered any words.")

    print("Enter another string or enter 'E' to exit.")

    string = input()

    if string in ['E', 'e']:
        break
