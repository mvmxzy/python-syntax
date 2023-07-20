def print_upper_words(words):
    """
        >>> print_upper_words(["Coding", "is", "very", "cool"])
        CODING
        IS
        VERY
        COOL
    """

    for word in words:
        print(word.upper())


def print_upper_words2(words):
    """
        >>> print_upper_words2(["egg", "edible", "Apple"])
        EGG
        EDIBLE
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    """
        >>> print_upper_words3(["egg", "edible", "Apple", "Eddie"],
        APPLE
        EDDIE
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
