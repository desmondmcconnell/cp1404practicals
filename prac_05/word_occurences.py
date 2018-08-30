"""Word Occurences Calculator"""


def main():
    string = input("Please enter a string:")
    print("Text: {}".format(string))
    words = sorted(string.split(" "))
    words_counts = generate_dictionary(words)
    print_dictionary(words_counts, words)


def generate_dictionary(words):
    words_counts = {}
    for word in words:
        if word in words_counts:
            words_counts[word] += 1
        else:
            words_counts[word] = 1
    return words_counts


def print_dictionary(words_counts, words):
    longest_word = determine_longest_word(words)
    for word in words_counts:
        print("{:{}}: {}".format(word, longest_word, words_counts[word]))


def determine_longest_word(words):
    long_word = 0
    for word in words:
        if len(word) > long_word:
            long_word = len(word)
    return long_word


main()

