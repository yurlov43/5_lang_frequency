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


def edit_text(text, unwanted_words):
    text = full_text.lower()
    for item in unwanted_words:
        text = text.replace(item, "")
    return text


def get_most_frequent_words(text, number_top_words):
    list_correct_words = text.split()
    counted_words = Counter(list_correct_words)
    return counted_words.most_common(number_top_words)


def print_list_words(list_words):
    print("Самые частые слова в тексте:")
    item = 1
    for word, number in list_words:
        print('{} {}. \"{}\" повторяется {} раз(а)'.format(
            "\t", item, word, number))
        item += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    arg = parser.parse_args()
    if not os.path.exists(arg.filepath):
        sys.exit("Ошибка: файл не найден!")
    text_encoding = get_text_encoding(arg.filepath)
    full_text = load_text(arg.filepath, text_encoding)
    unwanted_words = [
        "—", "-", ".", ",", "!", "?", ":", ";",
        "{", "}", "[", "]", "(", ")", "\""]
    correct_text = edit_text(full_text, unwanted_words)
    number_top_words = 10
    list_top_words = get_most_frequent_words(correct_text, number_top_words)
    print_list_words(list_top_words)
