"""Build a dictionary mapping words to their lengths."""


def long_cat_is_long(text):
    """Return each lowercase word and its length after removing punctuation."""
    words = (
        "".join(letter for letter in word if letter.isalpha())
        for word in text.lower().split()
    )
    return {word: len(word) for word in words if word}


count_words = long_cat_is_long


if __name__ == "__main__":
    print(long_cat_is_long("You see, wire telegraph is a very, very long cat."))
