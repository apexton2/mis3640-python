from string import ascii_lowercase

LETTERS = {letter: index for index, letter in enumerate(ascii_lowercase, start=1)}


def alphabet_position(text):
    text = text.lower()

    numbers = [LETTERS[character] for character in text if character in LETTERS]

    return sum(numbers)


print(alphabet_position('bananas'))
print(alphabet_position('rice'))
print(alphabet_position('paprika'))
print(alphabet_position('potatochips'))
print(alphabet_position('bananas rice paprika potatochips'))
