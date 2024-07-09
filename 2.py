import random
import nltk
nltk.download('words')
from nltk.corpus import words

def generate_random_words(num_words):
    word_list = words.words()
    random_words = random.sample(word_list, num_words)
    return random_words

def write_words_to_file(words, file_name):
    with open(file_name, 'w') as file:
        file.write(' '.join(words))

def main():
    num_words = 16
    file_name = 'random_words.txt'
    random_words = generate_random_words(num_words)
    write_words_to_file(random_words, file_name)
    print(f"Generated words: {' '.join(random_words)}")
    print(f"Words have been written to {file_name}")
main()
