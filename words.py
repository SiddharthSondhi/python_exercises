#!/usr/bin/env python3
"""Retrieve and print words from a URL.

Usage:
    python3 words.py <URL>

"""


import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.

    Arguments:
        url: The URL of a UTF-8 document.

    Returns:
        A lost of strings containing the words from the documents.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Prints items one per line.

    Arguments:
        An iterable series of printable items.

    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from a url.

    Args:
        url: The URL of a UTF-8 document.
    """
    words = fetch_words(url)
    print_items(words)


# __name__ is equal to "__main__" when "words" is being run directly through the system shell.
# If "words" is being run as a script (being imported) then __name__ is equal to "words"
if __name__ == "__main__":
    # sys.argv[1] is used to allow commandline arguments which is required here to enter the url.
    main(sys.argv[1])

# example url : "http://sixty-north.com/c/t.txt"
