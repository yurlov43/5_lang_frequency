import argparse
import os.path
import sys
import chardet
from collections import Counter
import re


def parser_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filepath",
        help="The path to the text file")
    return parser.parse_args()


def get_text_encoding(filepath):
    with open(filepath, "rb") as text_file:
        return chardet.detect(text_file.read())["encoding"]


def load_text(filepath, text_encoding):
    with open(filepath, "r", encoding=text_encoding) as text_file:
        return text_file.read()


def remove_unwanted_symbols(text):
    return re.sub(r"[^a-zA-Zа-яА-Я]", " ", text.lower())


def get_most_frequent_words(text, number_words):
    counted_words = Counter(text.split())
    return counted_words.most_common(number_words)


def print_list_words(list_words):
    print("Самые частые слова в тексте:")
    for number, (word, frequency) in enumerate(list_words, start=1):
        print('{} {}. \"{}\" повторяется {} раз(а)'.format(
            "\t", number,  word, frequency))


if __name__ == '__main__':
    arguments = parser_arguments()
    if not os.path.exists(arguments.filepath):
        sys.exit("Ошибка: файл не найден!")
    text_encoding = get_text_encoding(arguments.filepath)
    full_text = load_text(arguments.filepath, text_encoding)
    full_text = remove_unwanted_symbols(full_text)
    number_frequent_words = 10
    list_frequent_words = get_most_frequent_words(
        full_text, number_frequent_words)
    print_list_words(list_frequent_words)
