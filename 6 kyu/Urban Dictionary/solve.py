import re


class WordDictionary:
    def __init__(self):
        self.__words__ = set()

    def add_word(self, word):
        self.__words__.add(word)

    def search(self, pattern):
        for word in self.__words__:
            if re.search(r'^' + pattern + '$', word):
                return True
        return False
