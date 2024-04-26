import random
import os
import time
import psutil


class Word:
    def __init__(self, word: str):
        self.word = word.strip().lower()

    def is_valid(self, board: 'Board') -> bool:
        return 4 <= len(self.word) <= 9 and board.grid[1][1] in self.word and \
               all(self.word.count(char) <= (board.grid[0] + board.grid[1] + board.grid[2]).count(char) for char in set(self.word)) 

    def __repr__(self) -> str:
        return self.word

    def __eq__(self, other_word: 'Word') -> bool:
        return isinstance(other_word, Word) and self.word == other_word.word


class Board:
    def __init__(self, grid: list[list[str]] = None):
        self.grid = grid if grid is not None else self.generate_grid()

    def __str__(self) -> str:
        return f'Your board is:\n{"".join(self.grid[0])}\
\n{"".join(self.grid[1])}\n{"".join(self.grid[2])}'

    @staticmethod
    def generate_grid():
        vowels = ["A", "O", "U", "E", "I"]
        consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']  
        return [random.choices(consonants, k=2) + [random.choice(vowels)] for _ in range(3)] 

    def get_words(self, filename: str) -> list['Word']:
        with open(filename, 'r', encoding="utf-8") as file:
            return [Word(word) for word in file.readlines()[3:] if 4 <= len(word.strip().lower()) <= 9 and Word(word).is_valid(self)]


class TargetGame:
    def __init__(self, filename: str, board: list[list[str]] = None, words: list[str] = None):
        self.board = Board(board)
        self.__possible_words = self.board.get_words(filename)
        self.__user_words = [Word(w.strip().lower()) for w in self.get_user_words(words)]

    def get_user_words(self, val: list[str]) -> list[str]:
        if val:
            return val

        print(f'{self.board}\nPlease, suggest your words.\nWhen you finished, hit: *nix: Ctrl-D, Windows: Ctrl-Z+Return')
        try:
            return [input().strip().lower() for _ in range(int(1e6)) if len(_) >= 4]  
        except EOFError:
            return []  

    @property
    def user_words(self):
        return self.__user_words

    @user_words.setter
    def user_words(self, value : list[str]):
        self.__user_words = [Word(el.strip().lower()) for el in value]

    @property
    def correct_user_words(self):
        if not hasattr(self, '_correct_user_words'):
            self._correct_user_words = [word for word in self.__user_words if word in self.__possible_words]
        return self._correct_user_words

    def __str__(self):
        correct_count = len(self.correct_user_words)
        possible_count = len(self.__possible_words)
        return f'---------Game results---------:\n\
The list of your words is:\n\
{self.user_words}\n\
The list of your correct words:\n\
{self.correct_user_words}\n\
The number of possible words: {possible_count}\n\
You guess {correct_count * 100 // possible_count if possible_count else 0}% of possible words.'


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
