from collections import Counter
from re import findall



def count_words(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read()
    words = findall(r'\w+', text.lower())
    return Counter(words)

def most_common_words_in_file(filename, n):
    counts = count_words(filename)
    for word, count in [['Word', 'Count']] + counts.most_common(n):
        print(f'{word:>15} {count:>6}')


if __name__ == "__main__":

    try:
        file = input("What file would you like to read? ")
        num_words = int(input('How many words would you like to find?: '))
        most_common_words_in_file(file, num_words)
    except FileNotFoundError:
        print("File not found, please ensure that you have referenced a file that exists.")
    except:
        print("An error occurred")
