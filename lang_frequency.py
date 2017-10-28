import argparse
import os.path
import sys
import chardet
from collections import Counter


def get_text_encoding(filepath):
    with open(filepath, "rb") as text_file:
        return chardet.detect(text_file.read())["encoding"]


def load_text(filepath, text_encoding):
    with open(arg.filepath, "r", encoding=text_encoding) as text_file:
        return text_file.read()


def remove_symbols(text, symbols):
    text = text.lower()
    for symbol in symbols:
        text = text.replace(symbol, "")
    return text


def get_most_frequent_words(text, number_words):
    list_all_words = text.split()
    counted_words = Counter(list_all_words)
    return counted_words.most_common(number_words)


def print_list_words(list_words):
    numbered_list_words = enumerate(list_words, start=1)
    print("Самые частые слова в тексте:")
    for number, word in numbered_list_words:
        print('{} {}. \"{}\" повторяется {} раз(а)'.format(
            "\t", number, word[0], word[1]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    arg = parser.parse_args()
    if not os.path.exists(arg.filepath):
        sys.exit("Ошибка: файл не найден!")
    text_encoding = get_text_encoding(arg.filepath)
    full_text = load_text(arg.filepath, text_encoding)
    unwanted_symbols = [
        "—", "-", ".", ",", "!", "?", ":", ";",
        "{", "}", "[", "]", "(", ")", "\""]
    full_text = remove_symbols(full_text, unwanted_symbols)
    number_frequent_words = 10
    list_frequent_words = get_most_frequent_words(
        full_text, number_frequent_words)
    print_list_words(list_frequent_words)
