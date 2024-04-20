"""Caeser"""
import os
import time
import psutil

def caesar_encode(message: str, key: int) -> str:
    """
    (str, int) -> str
    Функція кодує повідомлення шифром Цезаря.

    >>> caesar_encode("computer", 3)
    'frpsxwhu'
    >>> caesar_encode("Zebra", 2)
    'Bgdtc'
    """
    result = ''
    for char in message:
        if char.islower():
            result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        elif char.isupper():
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            result += char
    return result

def caesar_decode(message: str, key: int) -> str:
    """
    (str, int) -> str
    Функція декодує повідомлення, закодоване шифром Цезаря.

    >>> caesar_decode('frpsxwhu', 3)
    'computer'
    >>> caesar_decode('Bgdtc', 2)
    'Zebra'
    """
    return caesar_encode(message, -key) 

#testing time and code
process = psutil.Process(os.getpid())
TIME = 0
MEMORY = 0

for el in range(1000):
    memory_before = process.memory_info().rss / (1024 )
    start_time = time.time()

    # caesar_encode('weare dedicated to addressing food insecurity for homebound seniors, weare dedicated to addressing food insecurity for homebound seniors', 3)

    # caesar_encode('computer', 3)

    # caesar_decode('weare dedicated to addressing food insecurity for homebound seniors, weare dedicated to addressing food insecurity for homebound seniors', 3)

    # caesar_decode('computer', 3)

    end_time = time.time()
    memory_after = process.memory_info().rss / (1024)
    elapsed_time = (end_time - start_time) * 1000
    TIME += elapsed_time
    MEMORY += memory_after - memory_before

print("Execution time:", TIME)
print("Difference:", MEMORY, "KB")
