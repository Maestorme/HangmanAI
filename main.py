from nltk.corpus    import words
from string         import ascii_uppercase
import requests
import time


def get_freq_list():
    letter_to_frequency = {letter: 0 for letter in ascii_uppercase}
    for word in words.words():
        for character in word:
            try:
                letter_to_frequency[character.upper()] += 1
            except KeyError:
                continue
    sorted_by_value = sorted(letter_to_frequency.items(), key=lambda kv: kv[1], reverse=True)
    return ''.join([letter for letter,frequency in sorted_by_value])


if __name__ == "__main__":
    print(get_freq_list())

