import os
import time
import psutil

LOWER_OFFSET = ord('a')
UPPER_OFFSET = ord('A')
ALPHABET_SIZE = 26

def build_shift_table(key):
    lower_table = [chr((ord(c) - LOWER_OFFSET + key) % ALPHABET_SIZE + LOWER_OFFSET) for c in 'abcdefghijklmnopqrstuvwxyz']
    upper_table = [chr((ord(c) - UPPER_OFFSET + key) % ALPHABET_SIZE + UPPER_OFFSET) for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    return lower_table, upper_table

def caesar_encode(message: str, key: int) -> str:
    """
    (str, int) -> str
    The function accepts a message as the first argument and a key 
    as the second. The function returns a string -- moving each letter 
    of the message text a fixed number (called the key) of positions 
    in the alphabet.
    
    >>> caesar_encode("computer", 3)
    'frpsxwhu'
    >>> caesar_encode("zebra", 2)
    'bgdtc'

    """
    shift_table_encode, _ = build_shift_table(key)
    result = []
    for i in message:
        if i.isalpha():
            if i.islower():
                result.append(shift_table_encode[ord(i) - LOWER_OFFSET])
            else:
                result.append(shift_table_encode[ord(i) - UPPER_OFFSET + ALPHABET_SIZE])
        else:
            result.append(i)
    return ''.join(result)

def caesar_decode(message: str, key: int) -> str:
    """
    (str, int) -> str
    The function takes a message as the first argument and a key 
    as the second. The function decrypts the string — moving each 
    letter of the message text to a fixed number (called a key) of 
    positions in the alphabet.

    >>> caesar_decode('frpsxwhu', 3)
    'computer'
    >>> caesar_decode('bgdtc', 2)
    'zebra'

    """
    shift_table_decode, _ = build_shift_table(-key)
    result = []
    for i in message:
        if i.isalpha():
            if i.islower():
                result.append(shift_table_decode[ord(i) - LOWER_OFFSET])
            else:
                result.append(shift_table_decode[ord(i) - UPPER_OFFSET + ALPHABET_SIZE])
        else:
            result.append(i)
    return ''.join(result)

# testing time and memory
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
