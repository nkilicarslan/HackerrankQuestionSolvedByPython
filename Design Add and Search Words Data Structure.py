import re
class WordDictionary:

    def __init__(self):
        self.hash_map = {}

    def addWord(self, word: str) -> None:
        self.hash_map[word] = 1

    def search(self, word: str) -> bool:
        if '.' not in word:
            if word in self.hash_map:
                return True
            else:
                return False
        else:
            for key in self.hash_map:
                if len(word) == len(key) and re.match(word, key):
                    return True
            return False

