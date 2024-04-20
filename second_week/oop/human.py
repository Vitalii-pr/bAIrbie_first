"""target game in oop"""

import random
import os
import time
import psutil

class Word:
    """class for words"""

    def __init__(self, word: str):
        self.word = word.strip().lower()

    def is_valid(self, board: 'Board') -> bool:
        """
        Method for checking if the word is valid for the given board
        """
        return all( [9 >= len((word := self.word.upper())) >= 4, board.grid[1][1] in word,\
                    all( word.count(el) <= sum(board.grid, []).count(el)\
                    for el in set(word) )])

    def __repr__(self) -> str:
        return self.word

    def __eq__(self, other_word: 'Word') -> bool:
        return isinstance(other_word, Word) and self.word == other_word.word


class Board:
    """class for the game board"""

    def __init__(self, grid: list[list[str]] = None):
        self.__grid = grid if grid is not None else self.generate_grid()

    def __str__(self) -> str:
        return f'Your board is:\n{"".join(self.grid[0])}\
\n{"".join(self.grid[1])}\n{"".join(self.grid[2])}'

    @property
    def grid(self):
        """
        property for the game board grid
        """
        return self.__grid

    @staticmethod
    def generate_grid():
        """
        static method for generating a random game board
        """
        voval = ["A", "O", "U", "E", "I"]
        consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J',\
    'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
        res = [[],[],[]]
        for i in range(3):
            vov = [random.choice(voval)]
            con = random.choices(consonants, k=2)
            res[i] = vov+con
        return res

    def get_words(self, filename: str) -> list['Word']:
        """
        method for getting all the words that follow the rules for the board
        """
        res = []
        with open(filename, 'r', encoding="utf-8") as file:
            lst = file.readlines()
            for i in lst[3:]:
                if 4 <= len(i) <= 9 and Word(i.strip().lower()).is_valid(self):
                    res.append(Word(i.strip().lower()))
        return res


class TargetGame:
    """class for the target game"""

    def __init__(self, filename: str, board: list[list[str]] = None, words: list[str] = None):
        self.board = Board(board)
        self.__possible_words = self.board.get_words(filename)
        self.__user_words = [Word(word.strip().lower()) for word in self.get_user_words(words)]

    def get_user_words(self, val: list[str]) -> list[str]:
        """
        method for getting the input guess from user
        """
        if val:
            return val
        print(f'{self.board}\nPlease, suggest your words.\n\
When you finished, hit: *nix: Ctrl-D, Windows: Ctrl-Z+Return')
        inp = []
        try:
            while True:
                x = input().strip().lower()
                if len(x)>=4:
                    inp.append(x)
        except EOFError:
            return inp

    @property
    def user_words(self):
        """
        property getter for the user words list
        """
        return self.__user_words

    @user_words.setter
    def user_words(self, value : list[str]):
        """
        property setter that adds guessed words to user words
        """
        self.__user_words = [Word(el.strip().lower()) for el in value]

    @property
    def correct_user_words(self):
        """
        property for all the right guessed words from user
        """
        return [word for word in self.__user_words if word in self.__possible_words]

    def __str__(self):
        return f'---------Game results---------:\n\
The list of your words is:\n\
{self.user_words}\n\
The list of your correct words:\n\
{self.correct_user_words}\n\
The number of possible words: {len(self.__possible_words)}\n\
You guess {len(self.correct_user_words)*100//len(self.__possible_words)}% of possible words.'


# Testing time and memory
process = psutil.Process(os.getpid())
TIME = 0
MEMORY = 0

for el in range(20):
    memory_before = process.memory_info().rss / (1024 )
    start_time = time.time()

    # game = TargetGame('en.txt', [['E', 'S', 'Z'], ['Y', 'C', 'I'], ['D', 'P', 'Y']], ['Dice', 'spIcy', 'float'])

    end_time = time.time()
    memory_after = process.memory_info().rss / (1024)
    elapsed_time = (end_time - start_time) * 1000
    TIME += elapsed_time
    MEMORY += memory_after - memory_before

print("Execution time:", TIME)
print("Difference:", MEMORY, "KB")
